import com.kms.katalon.core.webui.driver.DriverFactory
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.WebDriver
import org.openqa.selenium.chrome.ChromeDriver
import org.openqa.selenium.chrome.ChromeOptions

// Copy the path to chromedriver.exe
String pathToChromeDriver = "{katalon_installed_folder}\configuration\resources\drivers\chromedriver_win32\chromedriver.exe"
System.setProperty("webdriver.chrome.driver")

// It is important that this chromeProfilePath ends with User Data and not with the profile folder (Profile 2)
String chromeProfilePath = "C:\\Users\\thanhto\\AppData\\Local\\Google\\Chrome\\User Data\\";
ChromeOptions chromeProfile = new ChromeOptions();
chromeProfile.addArguments("user-data-dir=" + chromeProfilePath);
// Here you specify the actual profile folder (Profile 2)
chromeProfile.addArguments("profile-directory=Profile 2");

WebDriver driver = new ChromeDriver(chromeProfile);
driver.get("https://gmail.com/");
DriverFactory.changeWebDriver(driver)