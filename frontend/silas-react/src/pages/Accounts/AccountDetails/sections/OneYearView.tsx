// @ts-nocheck
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import { metricsLabels } from '../../../../metricsDescriptions';
import {
  rotateData,
  convertRotatedData,
  convertTableHeaders,
} from '../helpers';

import Claims from './oneYearSections/Claims';
import PropertyDamage from './oneYearSections/PropertyDamage';
import TechnicalData from './oneYearSections/TechnicalData';

import { formatToDollar } from '../../../../utils/formatters';

import Table from '../../../../components/Tables/Table';

interface OneYearViewProps {
  viewDetailsTable: boolean;
}

interface kpiMetricsTypes {
  label: string;
  value: number;
  format?: 'perc' | 'dollar';
}

interface TableRowItemType {
  item: string;
  year_minus_1: number;
  year_minus_2: number;
  year_minus_3: number;
  year_minus_4: number;
  year_minus_5: number;
}

type PieChartType = {
  data: any[];
  labels: string[];
};

type DataTableType = TableRowItemType[];

const OneYearView: React.FC<OneYearViewProps> = ({ viewDetailsTable }) => {
  const [gwpNwpValues, setGwpNwpValues] = useState<kpiMetricsTypes[] | null>(
    null,
  );
  const [rateValues, setRateValues] = useState<kpiMetricsTypes[] | null>(null);
  const [feesAndBrokerage, setFeesAndBrokerage] = useState<
    kpiMetricsTypes[] | null
  >(null);
  const [policyLimit, setPolicyLimit] = useState<kpiMetricsTypes[] | null>(
    null,
  );
  const [claimsChartData, setClaimsChartData] = useState<
    kpiMetricsTypes[] | null
  >(null);
  const [propertyDamageData, setPropertyDamageData] = useState<
    kpiMetricsTypes[] | null
  >(null);
  const [deductibleData, setDeductibleData] = useState<
    kpiMetricsTypes[] | null
  >(null);
  const [damagesBreakdown, setDamagesBreakdown] = useState<
    PieChartType[] | null
  >(null);
  const [aalData, setAalData] = useState<kpiMetricsTypes[] | null>(null);
  const [techAdequacyData, setTechAdequacyData] = useState<
    kpiMetricsTypes[] | null
  >(null);
  const [techRateValues, setTechRateValues] = useState<
    kpiMetricsTypes[] | null
  >(null);
  const [lineRateValues, setLineRateValues] = useState<
    kpiMetricsTypes[] | null
  >(null);

  const [tableHeaders, setTableHeaders] = useState(null);
  const [tableData, setTableData] = useState(null);

  const { accountId } = useParams();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [tableData, kpisData] = await Promise.all([
          axios.get(
            `/api/v1/acct_overview?company_id=${accountId}`,
          ),
          axios.get(
            `/api/v1/new_metrics?company_id=${accountId}`,
          ),
        ]);
        return [tableData.data, kpisData.data];
      } catch (e) {
        console.log('Error fetching data: ', e);
      }
    };

    fetchData()
      .then(([tableData, kpisData]: [DataTableType]) => {
        const { rotatedData, tableHeaders } = rotateData(tableData);
        const tableColumnHeaders = convertTableHeaders(tableHeaders);
        const rotatedTableData = convertRotatedData(rotatedData);

        setTableHeaders(tableColumnHeaders);
        setTableData(rotatedTableData);

        const companyMetrics = kpisData.company_metrics[0];
        setLineRateValues([
          {
            label: metricsLabels['rate_on_tiv'],
            value: companyMetrics.rate_on_tiv,
            format: 'perc',
          },
          {
            label: metricsLabels['rate_on_line'],
            value: companyMetrics.rate_on_line,
            format: 'perc',
          },
        ]);

        setGwpNwpValues([
          {
            label: metricsLabels['gwp'],
            value: companyMetrics.gwp,
            format: 'dollar',
          },
          {
            label: metricsLabels['nwp'],
            value: companyMetrics.nwp,
            format: 'dollar',
          },
        ]);

        setPolicyLimit([
          {
            label: metricsLabels['policy_limit'],
            value: companyMetrics.policy_limit,
            format: 'dollar',
          },
        ]);

        setDamagesBreakdown({
          // @ts-ignore
          data: [
            companyMetrics.business_interruption,
            companyMetrics.property_damage,
          ],
          labels: [
            metricsLabels['business_interruption'],
            metricsLabels['property_damage'],
          ],
        });

        setAalData([
          {
            label: metricsLabels['aal'],
            value: companyMetrics.aal,
            format: 'dollar',
          },
          {
            label: metricsLabels['aal_perc_gwp'],
            value: companyMetrics.aal_perc_gwp,
            format: 'perc',
          },
        ]);

        setTechAdequacyData([
          {
            label: metricsLabels['tech_price'],
            value: companyMetrics.tech_price,
            format: 'dollar',
          },
          {
            label: metricsLabels['technical_adequacy'],
            value: companyMetrics.technical_adequacy,
            format: 'perc',
          },
        ]);

        setRateValues([
          {
            label: metricsLabels['base_rate'],
            value: companyMetrics.base_rate,
            format: 'perc',
          },
          {
            label: metricsLabels['rate_change'],
            value: companyMetrics.rate_change,
            format: 'perc',
          },
        ]);

        setFeesAndBrokerage([
          {
            label: metricsLabels['fees_and_commissions'],
            value: companyMetrics.fees_and_commissions,
            format: 'perc',
          },
          {
            label: metricsLabels['brokerage'],
            value: companyMetrics.brokerage,
            format: 'perc',
          },
        ]);

        setPropertyDamageData([
          {
            label: metricsLabels['property_damage'],
            value: companyMetrics.property_damage,
            format: 'dollar',
          },
          {
            label: metricsLabels['business_interruption'],
            value: companyMetrics.business_interruption,
            format: 'dollar',
          },
        ]);
        setDeductibleData([
          {
            label: metricsLabels['bi_deductible'],
            value: companyMetrics.bi_deductible,
          },
          {
            label: metricsLabels['aop_deductible'],
            value: companyMetrics.aop_deductible,
            format: 'dollar',
          },
        ]);

        setClaimsChartData([
          {
            title: 'Claims Property Damage / Business Interruption',
            data: [
              companyMetrics.property_damage,
              companyMetrics.business_interruption,
            ],
            labels: ['Property Damage', 'Business Interruption'],
          },
          {
            title: 'Claims by Region',
            data: [73, 26, 37, 93],
            labels: ['Africa', 'Latin America', 'Europe', 'USA'],
          },
          {
            title: 'Claims by Loss Type',
            data: [
              companyMetrics.gct_cpy - companyMetrics.gct_cat,
              companyMetrics.gct_cat,
            ],
            labels: ['Non-CAT', 'CAT'],
          },
        ]);

        setTechRateValues([
          {
            label: metricsLabels['rate_change'],
            value: companyMetrics.rate_change,
            format: 'perc',
          },
          {
            label: metricsLabels['avg_rate_change'],
            value: companyMetrics.avg_rate_change,
            format: 'perc',
          },
        ]);
      })
      .catch((e) => {
        console.log(e);
      });
  }, [accountId]);

  console.log({
    viewDetailsTable,
    tableData,
  });

  return (
    <div id="one-year-view">
      <h2 className="text-title-md2 mb-4 font-semibold text-black dark:text-white">
          KPI Summary
        </h2>
      <Claims
        gwpNwpValues={gwpNwpValues}
        policyLimit={policyLimit}
        rateValues={rateValues}
        feesAndBrokerage={feesAndBrokerage}
      />
      {/* <GrossClaims claimsChartData={claimsChartData} /> */}
      <PropertyDamage
        propertyDamageData={propertyDamageData}
        deductibleData={deductibleData}
        claimsChartData={claimsChartData}
        damagesBreakdown={damagesBreakdown}
      />
      <TechnicalData
        aalData={aalData}
        techAdequacyData={techAdequacyData}
        techRateValues={techRateValues}
        lineRateValues={lineRateValues}
      />
      {viewDetailsTable && tableData ? (
        <div id="table_wrapper" className="bg-white">
          <Table columns={tableHeaders} data={tableData} />
        </div>
      ) : null}
    </div>
  );
};

export default OneYearView;
