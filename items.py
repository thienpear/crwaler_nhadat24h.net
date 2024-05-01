import scrapy #đưa vào project crawler này

class CrawlerItem(scrapy.Item): #khai báo các cột  có trong output
    Title = scrapy.Field()
    URL = scrapy.Field()
    Price = scrapy.Field()
    SquareFootage = scrapy.Field()
    Location = scrapy.Field()
    AccessRoadWidth = scrapy.Field()
    FrontageWidth = scrapy.Field()
    Direction = scrapy.Field()
    BuildingFloors = scrapy.Field()
    CarParkingSlots = scrapy.Field()
    Bedrooms = scrapy.Field()
    Bathrooms = scrapy.Field()
    Description = scrapy.Field()
    Category = scrapy.Field()

   