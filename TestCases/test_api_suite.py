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
        self.obj.get_pokemon_names_from_api()
