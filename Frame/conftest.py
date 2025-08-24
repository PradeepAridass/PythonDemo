import os

import pytest
from _pytest import reports
from selenium import webdriver
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )


@pytest.fixture(scope="function")
def browserInitialise(request):
    global driver
    browser_name = request.config.getoption("browser_name").lower()

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "ie":
        driver = webdriver.Ie()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get("https://rahulshettyacademy.com/angularpractice/shop")
    # driver.get("https://rahulshettyacademy.com/loginpagePractise")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver # Before test function execution
    driver.quit() # Post your test function execution

REPORTS_DIR = "/reports"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
        # Execute all other hooks to obtain the report object

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    # Check if the test failed during the call phase
    if report.when in ("setup","call"):
       xfail = hasattr(report, 'wasxfail')
       # Access the driver if the test used it
       if(report.skipped and xfail) or (report.failed and not xfail):
           # driver = item.funcargs.get("browser", None)
           # if driver:
               reports.dir = os.path.join(os.path.dirname(__file__), 'reports', 'screenshots')
               os.makedirs(REPORTS_DIR, exist_ok=True)

               # time_stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
               file_name = os.path.join(REPORTS_DIR, report.nodeid.replace("::", "_").replace("/", "_").replace("\\", "_")+ ".png")
               print("file name is "+ file_name)
               _capture_screenshot(file_name)
               # driver.save_screenshot(file_path)
               if os.path.exists(file_name):
                  html =(
                        f'<div>'
                        f'f<img src= "{file_name}" alt="screenshot" style="width:300px;height:200px; '
                        f'onclick="window.open(this.src)" align="right"/>'
                        f'</div>'
                  )
                  extra.append(pytest_html.extras.html(html))

       report.extra = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)

    

