import requests
import test_data
from PageBaseUtility.PageBase import PageBase


class ApiSuite(PageBase):

    def get_pokemon_names_from_api(self, pokemon_id):
        """
        This method will fetch Pokemon names from api
        :param pokemon_id: ID of the Pokemon in the API
        :return: string
        """
        self.log.info(f"Pokemon id is: {pokemon_id}")
        response = requests.get(test_data.POKE_API_URL.format(id=pokemon_id))
        data = response.json()
        pokemon_name = data['name']
        self.log.info(f"Pokemon name fetched from the API is: {pokemon_name}")
        return pokemon_name

