from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage={'root_dir': 'hasil'})
google_crawler.crawl(keyword='batik madura', max_num=500)

# from icrawler.builtin import GoogleImageCrawler

# google_crawler = GoogleImageCrawler(
#     feeder_threads=1,
#     parser_threads=2,
#     downloader_threads=4,
#     storage={'root_dir': 'your_image_dir'})
# filters = dict(
#     size='large',
#     color='orange',
#     license='commercial,modify',
#     date=((2017, 1, 1), (2017, 11, 30)))
# google_crawler.crawl(keyword='cat', filters=filters, max_num=1000, file_idx_offset=)