def test_create_user(client):
    query = """
    mutation {
        createUser(userDetails: {
            address: "0x3a96c519037e1a179C95634a96B3Ab0c7aE09a04",
            discordID: "875545081820622868"
        })
        {
            id
        }
    }
    """

    result = client.execute(query)
    assert result['data']['createUser']['id'] == 1


def test_get_user_list(client, user):
    query = """
    query {
        listUsers {
            address
        }
    }
    """

    result = client.execute(query)
    assert type(result['data']['listUsers']) == list


def test_get_single_user(client, user):
    query = """
    query {
        getSingleUser(userId: %s){
            address
        }
    }
    """ % user.id
    result = client.execute(query)

    assert result['data']['getSingleUser'] is not None
    assert result['data']['getSingleUser']['address'] == user.address
