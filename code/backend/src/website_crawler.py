"""
Website Crawler for SBYEC
Automatically fetches and updates content from sbyec.org
"""

import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
from urllib.parse import urljoin, urlparse


class SBYECWebCrawler:
    def __init__(self, base_url="https://sbyec.org", output_dir="data"):
        """Initialize the web crawler"""
        self.base_url = base_url
        self.output_dir = output_dir
        self.visited_urls = set()
        self.content_sections = []

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Key pages to crawl (based on website structure)
        self.important_pages = [
            "/",  # Home
            "/events/",  # Events page (most important for updates!)
            "/riding-lessons/",  # Lessons
            "/programs/4h-rein-shine-club/",
            "/programs/books-at-the-buckle/",
            "/programs/camps/",
            "/programs/equine-encounters/",
            "/programs/field-trips/",
            "/programs/volunteer/",
            "/services/facility-rental/",
            "/services/equine-boarding/",
            "/about/our-mission/",
            "/about/meet-our-team/",
            "/about/meet-the-herd/",
            "/about/contact-us/",
        ]

    def fetch_page(self, url):
        """Fetch a single page with error handling"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (compatible; SBYEC-Bot/1.0; +info@silverbuckleranch.org)'
            }
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def extract_content(self, html, url):
        """Extract meaningful content from HTML"""
        if not html:
            return None

        soup = BeautifulSoup(html, 'html.parser')

        # IMPROVED: Extract footer info BEFORE removing (contains address, contact)
        footer_info = []
        footer = soup.find('footer')
        if footer:
            # Look for address patterns
            address_text = footer.get_text()
            if '11611' in address_text or 'Brush Prairie' in address_text:
                footer_info.append("ADDRESS: 11611 NE 152nd Avenue, Brush Prairie, WA 98606")
            if '564' in address_text or '208-1315' in address_text:
                footer_info.append("PHONE: (564) 208-1315")
            if 'info@' in address_text:
                footer_info.append("EMAIL: info@silverbuckleranch.org")

        # Remove unwanted elements
        for element in soup(['script', 'style', 'nav', 'header', 'iframe', 'noscript']):
            element.decompose()

        # Extract page title
        title = soup.find('title')
        title_text = title.get_text().strip() if title else "No Title"

        # Extract main content (try body if nothing else works)
        main_content = soup.find('body')

        if not main_content:
            return None

        # Extract text content
        content_text = main_content.get_text(separator='\n', strip=True)

        # Clean up excessive whitespace
        lines = [line.strip() for line in content_text.split('\n') if line.strip()]
        clean_content = '\n'.join(lines)

        # IMPROVED: Add footer info at the top for all pages
        if footer_info:
            clean_content = '\n'.join(footer_info) + '\n\n' + clean_content

        # Create structured content block
        content_block = f"""
{'='*70}
PAGE: {title_text}
URL: {url}
LAST UPDATED: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'='*70}

{clean_content}

"""
        return content_block

    def crawl_page(self, relative_url):
        """Crawl a single page and extract content"""
        full_url = urljoin(self.base_url, relative_url)

        # Avoid duplicate crawling
        if full_url in self.visited_urls:
            return None

        print(f"Crawling: {relative_url}")
        self.visited_urls.add(full_url)

        # Fetch and parse
        html = self.fetch_page(full_url)
        if not html:
            return None

        # Extract content
        content = self.extract_content(html, full_url)
        if content:
            self.content_sections.append(content)

        # Be polite: add delay between requests
        time.sleep(1)

        return content

    def crawl_all(self):
        """Crawl all important pages"""
        print("\nStarting SBYEC Website Crawler...")
        print(f"Base URL: {self.base_url}")
        print(f"Output Directory: {self.output_dir}\n")

        start_time = time.time()

        # Crawl all important pages
        for page_url in self.important_pages:
            self.crawl_page(page_url)

        # Save all content to file
        output_file = os.path.join(self.output_dir, "sbyec_website_content.txt")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"SBYEC Website Content - Last Crawled: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*70 + "\n\n")
            f.write('\n'.join(self.content_sections))

        elapsed_time = time.time() - start_time

        print(f"\nCrawling Complete!")
        print(f"Pages crawled: {len(self.visited_urls)}")
        print(f"Content sections: {len(self.content_sections)}")
        print(f"Saved to: {output_file}")
        print(f"Time elapsed: {elapsed_time:.2f} seconds\n")

        return output_file

    def crawl_events_only(self):
        """Quick crawl of just the events page (for frequent updates)"""
        print("\nQuick Update: Fetching latest events...")

        events_content = self.crawl_page("/events/")

        if events_content:
            # Save events to separate file
            output_file = os.path.join(self.output_dir, "sbyec_events.txt")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(events_content)
            print(f"Events updated: {output_file}\n")
            return output_file
        else:
            print(f"Failed to fetch events\n")
            return None


def main():
    """Main function to run the crawler"""
    crawler = SBYECWebCrawler()

    # Full crawl
    crawler.crawl_all()

    print("TIP: Run this script regularly (e.g., daily) to keep content updated!")
    print("For quick updates, you can also crawl just the events page.")


if __name__ == "__main__":
    main()
