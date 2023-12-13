# Import thư viện requests để thực hiện các yêu cầu HTTP.
import requests
# Import thư viện re để xử lý các biểu thức chính quy.
import re

# Định nghĩa lớp WebCrawler để thực hiện việc thu thập dữ liệu trên web.
class WebCrawler:

    # Hàm khởi tạo của lớp.
    def __init__(self):
        # Tạo một danh sách rỗng để theo dõi các trang web đã được khám phá.
        self.discovered_websites = []

    # Phương thức để bắt đầu quá trình thu thập từ một URL ban đầu.
    def crawl(self, start_url):
        # Tạo một hàng đợi và thêm URL ban đầu vào hàng đợi.
        queue = [start_url]
        # Đánh dấu URL ban đầu là đã được khám phá.
        self.discovered_websites.append(start_url)

        # Lặp cho đến khi hàng đợi không còn URL nào.
        while queue:
            # Lấy URL đầu tiên từ hàng đợi.
            actual_url = queue.pop(0)
            # In URL đó ra màn hình.
            print(actual_url)

            # Đọc nội dung HTML từ URL hiện tại.
            actual_url_html = self.read_raw_html(actual_url)

            # Tìm và xử lý tất cả các liên kết từ HTML đó.
            for url in self.get_links_from_html(actual_url_html):
                # Nếu URL chưa được khám phá, thêm nó vào danh sách và hàng đợi.
                if url not in self.discovered_websites:
                    self.discovered_websites.append(url)
                    queue.append(url)

    # Phương thức để tìm tất cả các liên kết HTTP/HTTPS trong mã HTML.
    def get_links_from_html(self, raw_html):
        # Sử dụng biểu thức chính quy để tìm các liên kết.
        return re.findall("https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", raw_html)

    # Phương thức để đọc nội dung HTML từ một URL.
    def read_raw_html(self, url):
        # Khởi tạo một chuỗi trống để chứa HTML.
        raw_html = ''

        try:
            # Thử gửi yêu cầu HTTP GET và lấy nội dung văn bản.
            raw_html = requests.get(url).text
        except Exception as e:
            # Nếu có lỗi, bỏ qua và giữ chuỗi HTML trống.
            pass

        return raw_html


# Điểm bắt đầu chính của script.
if __name__ == '__main__':
    # Tạo một đối tượng WebCrawler.
    crawler = WebCrawler()
    # Bắt đầu quá trình thu thập dữ liệu từ URL chỉ định.
    crawler.crawl('https://www.cnn.com')
