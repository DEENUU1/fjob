from abc import abstractmethod, ABC
from ...models import PageContent
import logging


logging.basicConfig(
    filename="../logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class GetContentStrategy(ABC):
    """
    Abstract base class for retrieving and saving content.

    Methods:
    - fetch_content: Retrieves the content.
    - save_to_db: Saves the content to a database.
    - __len__: Returns the length of the content.
    """

    def __init__(self, website: str, base_url: str):
        self.data = []
        self.website = website
        self.base_url = base_url

    @abstractmethod
    def fetch_content(self):
        pass

    def save_to_db(self) -> bool:
        logging.info(f"Start saving page content for {self.website}")
        if not self.data:
            logging.info(f"Failed to save page content for {self.website}")
            return False

        try:
            for content in self.data:
                PageContent.objects.create(
                    content=content,
                    website=self.website,
                )

            logging.info(f"Page content saved for {self.website}")
            return True
        except Exception as e:
            logging.error(f"Failed to save page content for {self.website}: {e}")

    def __len__(self):
        return len(self.data)

    def save_to_db_json(self, data) -> bool:
        logging.info(f"Start saving page content for {self.website}")
        if not data:
            logging.info(f"Failed to save page content for {self.website}")
            return False
        try:
            PageContent.objects.create(
                content_json=data,
                website=self.website,
            )
            logging.info(f"Page content saved for {self.website}")
            return True
        except Exception as e:
            logging.error(f"Failed to save page content for {self.website}: {e}")
