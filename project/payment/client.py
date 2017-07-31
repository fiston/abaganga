import requests
from project.exception_handling import ApiError


def make_mobile_payment(amount, phone, names):
    task = {
    "names": names,
    "phone": phone,
    "amount": amount
    }
    resp = requests.post('http://127.0.0.1:8000/mobilepayment/', json=task, auth=('tst_user', '@ssSuper!135'))
    print resp.text+" ------------------"+str(resp.status_code)
    if resp.status_code != 201:
        raise ApiError('POST /mobilepayment/ {}'.format(resp.status_code))
    print('Created task. ID: {}'.format(resp.json()["id"]))
