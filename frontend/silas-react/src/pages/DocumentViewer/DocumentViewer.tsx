import { useState } from 'react';

import Layout from '../../layout/Layout';
import ReactDiffViewer from 'react-diff-viewer-continued';

import { Tabs, Tab } from '../../components/Tabs';
import FilesUploader from '../../components/FilesUploader/FilesUploader';

const DocumentViewer = () => {
  const [requestSuccess, setRequestSuccess] = useState(false);
  const [comparedDocument, setComparedDocument] = useState<{original: string; current:string;} | null>();

  const [originalDocument, setOriginalDocument] = useState<string | null>(null);
  const [recentDocument, setRecentDocument] = useState<string | null>(null);

  return (
    <Layout>
      <div className="mx-auto max-w-270">
        <div className="grid grid-cols-5 gap-8">
          <div className="col-span-5">
            <div className="rounded-sm border border-stroke bg-white shadow-default dark:border-strokedark dark:bg-boxdark">
              <div className="border-b border-stroke py-4 px-7 dark:border-strokedark">
                <h3 className="font-medium text-black dark:text-white">
                  Document Viewer
                </h3>
              </div>
              <div className="h-full p-7">
                {requestSuccess ? (
                  <>
                    <button
                      className="flex justify-center rounded bg-primary mb-4 py-2 px-6 font-medium text-gray hover:bg-opacity-90"
                      onClick={() => setRequestSuccess(false)}
                    >
                      New Document Comparison
                    </button>
                    <Tabs>
                      <Tab label="Text Diff View">
                        <div className="py-4">
                          <ReactDiffViewer
                            oldValue={comparedDocument?.original}
                            newValue={comparedDocument?.current}
                            splitView={true}
                          />
                        </div>
                      </Tab>
                      <Tab label="PDF View">
                        <div className="py-4">
                          <div className="flex h-screen">
                            <div className="w-full mx-2">
                              <iframe
                                src={originalDocument || ''}
                                title="Previous Document"
                                style={{ width: '100%', height: '100%' }}
                                frameBorder="0"
                              />
                            </div>
                            <div className="w-full mx-2">
                              <iframe
                                src={recentDocument || ''}
                                title="Current Document"
                                style={{ width: '100%', height: '100%' }}
                                frameBorder="0"
                              />
                            </div>
                          </div>
                        </div>
                      </Tab>
                    </Tabs>
                  </>
                ) : (
                  <FilesUploader
                    setRequestSuccess={setRequestSuccess}
                    setComparedDocument={setComparedDocument}
                    setOriginalDocument={setOriginalDocument}
                    setRecentDocument={setRecentDocument}
                  />
                )}
              </div>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
};

export default DocumentViewer;
