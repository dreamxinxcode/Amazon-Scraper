import requests
from bs4 import BeautifulSoup

LOGO = """\033[95m
         +hmNNmds.   .ddy:ymNmy--ymNmh:    /hmNNNds-    :ddddddddd/  .ohmNNds-   `ddy-smNmd+
        yNNhoohNNd   .NNNmsohNNmNyoyNNN-  sNNhooyNNm`   :hhhhhNNNN/ /mNNhsymNNs  `mNmmyosmNNo
        .:/   .NNN`  .NNN/  `mNNo   dNN/  .:/`  .mNN-       .yNNm: .mNN:   .dNN+ `mNN+   oNNh
         :oydmNNNN`  .NNN`   mNN:   yNN+   :oyhmNNNN-      :mNNy`  +NNh     oNNh `mNN.   /NNh
       `hNNy+:-NNN`  .NNN    mNN-   yNN+  hNNy+:.mNN.     sNNm+    /NNd     oNNy `mNN`   /NNh
       :NNd   -NNN.  .NNN    mNN-   yNN+ -NNm   .mNN.   .hNNd-`````.mNN+   -mNN: `mNN`   /NNh
       .mNNhsymmNN-  .NNN    mNN-   yNN+ `mNNhsymmNN:   dNNmdhyyydd -dNNmhdNNm/  `mNN`   /NNh
        .ohdhs-:yy/  `yyy    syy.   +yy:  .ohdhs::yy+   ::-...--. -   :shdhy+`    syy`   -yyo
                   -:-..`                               ::::::/// \033[1m\033[94mDeveloped by:\033[0m Brandon Lecky\033[95m
                    `.:///:-..`                       ``..--.`//-
                       `.-://///::--..````````..--:://///:-.`:/-
                           `.-://///////////////////::-.`   -:.
                                ``...----------..``
\033[0m
"""
class Amazon:
    """Uses BeautifulSoup to web scrape Amazon webpages for data.
        - Handle for pages with no prices
        - Handle for loss of connection
    """
    def __init__(self, URL):
        self.URL = URL
        self.USER_AGENT = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}
        self.page = requests.get(self.URL, headers=self.USER_AGENT)
        self.presoup = BeautifulSoup(self.page.content, "html.parser")
        self.soup = BeautifulSoup(self.presoup.prettify(), "html.parser") 
    
    def gather_data(self):
        self.title = self.soup.find(id="productTitle").get_text()
        self.price = self.soup.find(id="price_inside_buybox").get_text()
        self.seller = self.soup.find(id="sellerProfileTriggerId").get_text()
        #self.description = self.soup.find(id="productDescription").get_text()
        self.availability = self.soup.find(id="availability").text()
        self.reviews = self.soup.find(id="acrCustomerReviewText").text()

    def show_data(self):
        try:
            print(f"\033[1m\033[95m" + self.title.strip() + "\033[0m")
            print("\033[1m\033[95mPrice: \033[0m" + self.price.strip())
            print("\033[1m\033[95mSeller: \033[0m" + self.seller.strip())
            print("\n \033[1m\033[95mAvailability: \n" + self.availability())
            print("\033[1m\033[95mReviews: \033[0m" + self.reviews.strip())
        except AttributeError:
            print("[\033[95m*\033[0m]Error")

def main():
    print(LOGO)
    URL = input("\033[1m\033[95mAmazon URL: \033[0m")
    print(f"\n[\033[95m*\033[0m] \033[1m\033[95mGathering data from:\033[0m {URL} \n\n")
    product = Amazon(URL)
    product.gather_data()
    product.show_data()

if __name__ == "__main__":
    main()
