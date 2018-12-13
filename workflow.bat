python CornBasis_cleandata.py
copy "E:\Desktop\PyCode\cleandata_basis2.xlsx" "E:\Desktop\fhzbWeb\report\cleandata_basis.xlsx"
copy "E:\Desktop\uads\AnalysisReport\CornData.xlsx" "E:\Desktop\fhzbWeb\report\CornData.xlsx"
copy "E:\Desktop\uads\AnalysisReport\CornTempRes.xlsx" "E:\Desktop\fhzbWeb\report\CornTempRes.xlsx"

pscp "E:\Desktop\fhzbWeb\report\cleandata_basis.xlsx" ubuntu@111.230.170.168:/home/ubuntu/fhzbWeb/report/
pscp "E:\Desktop\fhzbWeb\report\CornData.xlsx" ubuntu@111.230.170.168:/home/ubuntu/fhzbWeb/report/
pscp "E:\Desktop\fhzbWeb\report\CornTempRes.xlsx" ubuntu@111.230.170.168:/home/ubuntu/fhzbWeb/report/

pause()