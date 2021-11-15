pytest -v -s -m "sanity" --html=./Reports/report_chrome.html testCases/ --browser Chrome


rem pytest -v -s -m "sanity" --html=./Reports/report_firefox.html testCases/ --browser Firefox


rem pytest -v -s -m "sanity or regression" --html=./Reports/report.html testCases/ --browser Chrome
rem pytest -v -s -m "sanity and regression" --html=./Reports/report.html testCases/ --browser Chrome
rem pytest -v -s -m "regression" --html=./Reports/report.html testCases/ --browser Chrome