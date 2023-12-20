<<<<<<< HEAD
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv


class BoxofficeCrawlerPipeline:

    def __init__(self):
        self.csvwriter = csv.writer(
<<<<<<< HEAD
            open("boxoffice2000_2022.csv", "w", newline=''))
=======
            open("boxoffice_1990_2022.csv", "w", newline=''))
>>>>>>> 8036ffbd0bc95fc8bf1cd15f679204a4e88c9006
        self.csvwriter.writerow(["title", "domestic_revenue", "world_revenue", "distributor",
                                "opening_revenue", "opening_theaters", "budget", "MPAA", "genres", "in_release","release_date"])

    def process_item(self, item, spider):
        row = []
        row.append(item["title"])
        row.append(item["domestic_revenue"])
        row.append(item["world_revenue"])
        row.append(item["distributor"])
        row.append(item["opening_revenue"])
        row.append(item["opening_theaters"])
        row.append(item["budget"])
        row.append(item["MPAA"])
        row.append(item["genres"])
        row.append(item["in_release"])
        row.append(item["release_date"])
        self.csvwriter.writerow(row)
        return item
=======
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv


class BoxofficeCrawlerPipeline:

    def __init__(self):
        self.csvwriter = csv.writer(
            open("boxoffice_1990_2022.csv", "w", newline=''))
        self.csvwriter.writerow(["title", "domestic_revenue", "world_revenue", "distributor",
                                "opening_revenue", "opening_theaters", "budget", "MPAA", "genres","running_time", "in_release","release_date"])

    def process_item(self, item, spider):
        row = []
        row.append(item["title"])
        row.append(item["domestic_revenue"])
        row.append(item["world_revenue"])
        row.append(item["distributor"])
        row.append(item["opening_revenue"])
        row.append(item["opening_theaters"])
        row.append(item["budget"])
        row.append(item["MPAA"])
        row.append(item["genres"])
        row.append(item["running_time"])
        row.append(item["in_release"])
        row.append(item["release_date"])
        
        self.csvwriter.writerow(row)
        return item
>>>>>>> d9aefeb7390689c0e1f1a12d905964a735950e9a
