"""
Automated Content Updater for SBYEC Chatbot
Runs the crawler periodically and updates the chatbot's knowledge base
"""

import schedule
import time
from datetime import datetime
import os
import sys
from website_crawler import SBYECWebCrawler


class AutoUpdater:
    def __init__(self, update_interval_hours=24):
        """
        Initialize the auto-updater

        Args:
            update_interval_hours: How often to update (default: 24 hours)
        """
        self.update_interval_hours = update_interval_hours
        self.crawler = SBYECWebCrawler()
        self.last_update = None

    def full_update(self):
        """Perform a full website crawl and update"""
        print(f"\n{'='*70}")
        print(f"🔄 SCHEDULED FULL UPDATE - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*70}")

        try:
            # Run the crawler
            output_file = self.crawler.crawl_all()
            self.last_update = datetime.now()

            print(f"✅ Update successful at {self.last_update.strftime('%H:%M:%S')}")
            print(f"📢 Chatbot will use updated content on next restart\n")

            return True
        except Exception as e:
            print(f"❌ Update failed: {e}\n")
            return False

    def quick_events_update(self):
        """Quick update of just the events page"""
        print(f"\n{'='*70}")
        print(f"⚡ QUICK EVENTS UPDATE - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*70}")

        try:
            output_file = self.crawler.crawl_events_only()
            if output_file:
                print(f"✅ Events updated successfully\n")
                return True
            else:
                print(f"⚠️  Events update had issues\n")
                return False
        except Exception as e:
            print(f"❌ Events update failed: {e}\n")
            return False

    def run_scheduled(self):
        """Run the updater on a schedule"""
        print("\n" + "="*70)
        print("🤖 SBYEC AUTO-UPDATER STARTED")
        print("="*70)
        print(f"📅 Full updates: Every {self.update_interval_hours} hours")
        print(f"📅 Events updates: Every 6 hours")
        print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*70 + "\n")

        # Run initial update
        print("🚀 Running initial update...")
        self.full_update()

        # Schedule recurring updates
        schedule.every(self.update_interval_hours).hours.do(self.full_update)
        schedule.every(6).hours.do(self.quick_events_update)

        print(f"⏳ Scheduler active. Press Ctrl+C to stop.\n")

        # Run scheduled jobs
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            print("\n\n👋 Auto-updater stopped by user")
            print(f"Last update was at: {self.last_update.strftime('%Y-%m-%d %H:%M:%S') if self.last_update else 'Never'}\n")

    def run_once(self):
        """Run a single update and exit"""
        print("🔄 Running one-time update...\n")
        self.full_update()
        print("✅ One-time update complete. Exiting.\n")


def main():
    """Main function"""
    import argparse

    parser = argparse.ArgumentParser(description='SBYEC Chatbot Auto-Updater')
    parser.add_argument(
        '--mode',
        choices=['scheduled', 'once', 'events-only'],
        default='once',
        help='Update mode: scheduled (continuous), once (single run), or events-only'
    )
    parser.add_argument(
        '--interval',
        type=int,
        default=24,
        help='Hours between full updates (default: 24)'
    )

    args = parser.parse_args()

    updater = AutoUpdater(update_interval_hours=args.interval)

    if args.mode == 'scheduled':
        updater.run_scheduled()
    elif args.mode == 'events-only':
        updater.quick_events_update()
    else:
        updater.run_once()


if __name__ == "__main__":
    main()
