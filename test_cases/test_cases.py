# import pytest
import requests
import json
# imports jsonpath


request_url = "http://127.0.0.1:8000/graphql"


def test_get_all_buisness():
    print("in-1")
    get_all_buisness = '''query {
    allBusiness {
        id
        name
        address
        ownerInfo
        employeeSize
    }
    }'''
    r = requests.get(request_url, json={'query': get_all_buisness})
    assert r.status_code == 200
    print(r.status_code)
    response = json.loads(r.text)
    print(response)


def test_get_all_buisness_by_id():
    print("in-2")
    get_all_buisness_by_id = '''query {
    business(businessId: 2) {
        id
        name
        ownerInfo
    }
    }'''
    r = requests.get(request_url, json={'query': get_all_buisness_by_id})
    assert r.status_code == 200
    print(r.status_code)
    response = json.loads(r.text)
    print(response)


def test_create_mutation():
    print("in-3")
    create_mutation = '''mutation createMutation {createBusiness(businessData: {name: "Nitin Khurana", address: "Mumbai,Maharashtra, India", ownerInfo: "Text test text", employeeSize: 25}) {
        business {
        name,
        address,
        ownerInfo,
        employeeSize
        }
    }
    }'''
    r = requests.post(request_url, json={'query': create_mutation})
    print(r.status_code)
    assert r.status_code == 200
    response = json.loads(r.text)
    print(response)


def test_update_mutation():
    print("in-4")
    update_mutation = '''mutation updateMutation {
    updateBusiness(businessData: {id: 7, name: "Karan sharma",
    address: "Mumbai, Maharashtra, India", ownerInfo: "Text test text",
    employeeSize: 25}) {
        business {
        name,
        address,
        ownerInfo,
        employeeSize
        }
    }
    }'''
    r = requests.post(request_url, json={'query': update_mutation})
    assert r.status_code == 200
    print(r.status_code)
    response = json.loads(r.text)
    print(response)


def test_delete_mutationn():
    print("in-5")
    delete_mutationn = '''mutation deleteMutation{
    deleteBusiness(id: 1) {
        business {
        id
        }
    }
    }'''
    r = requests.post(request_url, json={'query': delete_mutationn})
    assert r.status_code == 200
    print(r.status_code)
    response = json.loads(r.text)
    print(response)

if __name__ == '__main__':
    test_get_all_buisness()
    test_get_all_buisness_by_id()
    test_create_mutation()
    test_update_mutation()
    test_delete_mutationn()
