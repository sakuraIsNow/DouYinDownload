import browser_cookie3


def get_cookie_from_browser(browser_choice: str, domain: str = "") -> dict:
    """
    根据用户选择的浏览器获取domain的cookie。

    Args:
        browser_choice (str): 用户选择的浏览器名称

    Returns:
        str: *.domain的cookie值
    """

    if not browser_choice or not domain:
        return ""

    BROWSER_FUNCTIONS = {
        "chrome": browser_cookie3.chrome,
        "firefox": browser_cookie3.firefox,
        "edge": browser_cookie3.edge,
        "opera": browser_cookie3.opera,
        "opera_gx": browser_cookie3.opera_gx,
        "safari": browser_cookie3.safari,
        "chromium": browser_cookie3.chromium,
        "brave": browser_cookie3.brave,
        "vivaldi": browser_cookie3.vivaldi,
        "librewolf": browser_cookie3.librewolf,
    }
    cj_function = BROWSER_FUNCTIONS.get(browser_choice)
    cj = cj_function(domain_name=domain)
    cookie_value = {c.name: c.value for c in cj if c.domain.endswith(domain)}
    return cookie_value

print(get_cookie_from_browser('chrome', "douyin.com"))