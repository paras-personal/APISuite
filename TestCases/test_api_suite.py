import random
import pytest
from PageObjects.ApiSuite import ApiSuite


@pytest.mark.usefixtures('get_object')
class TestApiSuite:

    @pytest.fixture(scope='class')
    def get_object(self, request):
        obj = ApiSuite()
        request.cls.obj = obj


    ###################################################
    # TC 1:                                           #
    # Scenario: To get the pokemon name from the api  #
    ###################################################

    @pytest.mark.Apisuite
    def test_get_all_pokemon_names(self):
        """APISuite::To get the pokemon name from the api """
        pokemon_id = random.randint(1, 1281)
        name = self.obj.get_pokemon_names_from_api(pokemon_id)
        assert type(name) is str, f"{pokemon_id} does not have any pokemon associated in API"
