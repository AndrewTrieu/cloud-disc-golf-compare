from bulk_page_stucture.discking_scrape import get_data_discking
from bulk_page_stucture.discsport_scrape import get_data_discsport
from bulk_page_stucture.diskiundiskicesis_scrape import get_data_diskiundiskicesis
from bulk_page_stucture.par3_scrape import get_data_par3

from single_page_structure.latitude64_scrape import get_all_pages_latitude64, get_data_latitude64
from single_page_structure.powergrip_scrape import get_all_pages_powergrip, get_data_powergrip

get_data_discking()
get_data_discsport()
get_data_diskiundiskicesis()
get_data_par3()
all_urls_latitude64 = get_all_pages_latitude64()
get_data_latitude64(all_urls_latitude64)
all_urls_powergrip = get_all_pages_powergrip()
get_data_powergrip(all_urls_powergrip)