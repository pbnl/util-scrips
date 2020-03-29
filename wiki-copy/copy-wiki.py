import mechanicalsoup # Don’t forget to import the new module

if __name__ == "__main__":

    URL = "https://www.pbnl.de/index.php?title=Spezial:Anmelden"
    URLN = "https://intern.pbnl.de/index.php?title=Spezial:Anmelden"
    LOGIN = "USERNAME"
    PASSWORD = "PASSWORD"
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(URL, verify=False)
    browser.select_form('form[action="/index.php?title=Spezial:Anmelden&action=submitlogin&type=login"]')
    browser.get_current_form().print_summary()
    browser["wpName"] = LOGIN
    browser["wpPassword"] = PASSWORD
    browser.submit_selected()

    browserN = mechanicalsoup.StatefulBrowser()
    browserN.open(URLN, verify=False)
    browserN.select_form('form[action="/index.php?title=Spezial:Anmelden&action=submitlogin&type=login"]')
    browserN.get_current_form().print_summary()
    browserN["wpName"] = LOGIN
    browserN["wpPassword"] = PASSWORD
    browserN.submit_selected()

    page = browser.open("https://www.pbnl.de/intern/heimverzeichnis/Heimverzeichnis")
    links = page.soup.select("a")
    links = [link for link in links if "href" in link.attrs]

    for link in links:
        if input(link["href"] + "   :") == "y":
            url = "https://www.pbnl.de/index.php?title="+link["href"][1:]+"&action=edit"
            urlN = "https://intern.pbnl.de/index.php?title=" + link["href"][1:] + "&action=edit"
            page = browser.open(url)
            pageN = browserN.open(urlN)
            box = page.soup.select("#wpTextbox1")
            browserN.select_form("#editform")
            browserN["wpTextbox1"] = box[0].contents[0]
            browserN.submit_selected()
            print("Updated")
    print("Ready")