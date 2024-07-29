import React, { useEffect, useState } from 'react';
import { FeatureCollection } from '../../../map_data/london';
import './style.css';

import DeckGL, { GeoJsonLayer } from 'deck.gl';
import maplibregl from 'maplibre-gl';
import { Map } from 'react-map-gl';
import {
  LightingEffect,
  AmbientLight,
  _SunLight as SunLight,
} from '@deck.gl/core';

const INITIAL_VIEW_STATE = {
  latitude: 51.5145,
  longitude: -0.0815,
  zoom: 16,
  bearing: 5,
  pitch: 15,
};

interface MapComponentProps {
  mapData: FeatureCollection;
}

const MAP_STYLE =
  'https://basemaps.cartocdn.com/gl/positron-nolabels-gl-style/style.json';

const COLOR_SCALE = [
  [0, 130, 125],
  [28, 118, 111],
  [56, 106, 97],
  [84, 94, 83],
  [112, 82, 69],
  [140, 70, 55],
  [168, 58, 41],
  [196, 46, 27],
  [224, 34, 13],
  [255, 18, 0],
];

const ambientLight = new AmbientLight({
  color: [255, 255, 255],
  intensity: 1.0,
});

const dirLight = new SunLight({
  timestamp: Date.UTC(2019, 7, 1, 22),
  color: [255, 255, 255],
  intensity: 1.0,
  _shadow: true,
});

// need to revisit this
const landCover = [
  [
    [-0.1112, 51.5212],
    [-0.1112, 51.4975],
    [-0.0625, 51.5212],
    [-0.0625, 51.4975],
  ],
];

const formatAsDollar = (value) => {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
  }).format(value);
};

function getTooltip({ object }) {
  return (
    object && {
      html: `\
    <div>Building Type: ${object.properties.building_type}</div>
    <div>Insured Value: ${formatAsDollar(object.properties.insured_value)}</div>
    <div>Height: ${object.properties.height} m</div>
    `,
    }
  );
}

const FeatureToggle = ({ feature, onSelect, isSelected }) => {
  const handleClick = () => {
    onSelect(feature, !isSelected);
  };

  return (
    <div className="mx-2 flex items-center">
      <input
        className="mr-2"
        type="checkbox"
        checked={isSelected}
        onChange={handleClick}
      />
      <label>{feature}</label>
    </div>
  );
};

const FeatureSelector = ({ label, features, selectionHandler, initialSelection }) => {
  const [selectedFeatures, setSelectedFeatures] = useState(initialSelection);

  const handleSelect = (feature, isSelected) => {
    let selection;
    if (isSelected) {
      selection = [...selectedFeatures, feature];
    } else {
      selection = selectedFeatures.filter((item) => item !== feature);
    }
    setSelectedFeatures(selection);
    selectionHandler(selection);
  };

  return (
    <div className="flex">
      <h2>{label}</h2>
      {features.map((feature, index) => (
        <FeatureToggle
          key={index}
          feature={feature}
          isSelected={selectedFeatures.includes(feature)}
          onSelect={handleSelect}
        />
      ))}
    </div>
  );
};
// <div>Insurance Risk: ${object.properties.insurance_risk}</div>

const MapComponent: React.FC<MapComponentProps> = ({ mapData }) => {
  // const onClick = (info) => {
  //   if (info.object) {
  //     // eslint-disable-next-line
  //     alert(
  //       `${info.object.properties.name} (${info.object.properties.abbrev})`,
  //     );
  //   }
  // };

  // const [effects] = useState(() => {
  //   const lightingEffect = new LightingEffect({ ambientLight, dirLight });
  //   lightingEffect.shadowColor = [0, 0, 0, 0.5];
  //   return [lightingEffect];
  // });

  const features = [
    'Residential',
    'Commercial',
    'Office',
    'Historic',
    'Institutional',
  ];

  const [mapDisplayData, setMapDisplayData] = useState(null);
  const [selectedBuildingType, setSelectedBuildingType] = useState(features);

  useEffect(() => {
    const filteredIndexes = selectedBuildingType.map(
      (name) => features.indexOf(name) + 1,
    );

    const filteredFeatures =
      selectedBuildingType.length === 0
        ? mapData
        : mapData.features.filter((feature) =>
            filteredIndexes.includes(feature.properties.building_type),
          );

    setMapDisplayData(filteredFeatures);
  }, [selectedBuildingType]);

  const layers = [
    new GeoJsonLayer({
      id: 'geojson',
      data: mapDisplayData,
      opacity: 1,
      stroked: false,
      filled: true,
      extruded: true,
      wireframe: true,
      getElevation: (f) => f.properties.height * 1,
      getFillColor: (f) => COLOR_SCALE[f.properties.insurance_risk],
      getLineColor: [255, 255, 255],
      pickable: true,
    }),
  ];

  return (
    <div className="col-span-12 mb-4 xl:col-span-8 relative">
      <div className="flex flex-col justify-center mb-4 bg-white h-24 px-4">
        <h2 className="text-title-md2 font-semibold text-black dark:text-white">
          Insured Locations View
        </h2>
        <div className="flex mt-2">
          <FeatureSelector
            label={'Filter by Building Types:'}
            features={features}
            selectionHandler={(v) => setSelectedBuildingType(v)}
            initialSelection={selectedBuildingType}
          />
        </div>
      </div>
      <div className="parent">
        <DeckGL
          layers={layers}
          // effects={effects}
          initialViewState={INITIAL_VIEW_STATE}
          controller={true}
          getTooltip={getTooltip}
        >
          <Map
            reuseMaps
            mapLib={maplibregl}
            mapStyle={MAP_STYLE}
            preventStyleDiffing={true}
          />
        </DeckGL>
      </div>
    </div>
  );
};

export default MapComponent;
