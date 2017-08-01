import requests
from requests import HTTPError

from project.exception_handling import ApiError


def make_mobile_payment(amount, phone, names):
    try:
        amnt = int(amount)
        task = {
            "names": names,
            "phone": phone,
            "amount": amnt
        }
        resp = requests.post('http://127.0.0.1:8000/mobilepayment/', json=task, auth=('tst_user', '@ssSuper!135'))
        print resp.text + " ------------------" + str(resp.status_code)
        if resp.status_code != 200:
            print resp.status_code
            # raise HTTPError
        print('Created task. ID: {}'.format(resp.json()["id"]))
        return resp.status_code

    except requests.exceptions.RequestException as e:
        raise HTTPError
