import requests

API_URL="https://wordle.votee.dev:8000/random"


def guess_word(guess, seed=None, size=5):
    params={
        "guess":guess,
        "size":size
    }
    if seed is not None:
        params['seed']=seed

    response=requests.get(API_URL,params=params)
    if response.status_code==200:
        return response.json()
    else:
        response.raise_for_status()

def main():
    guess="theft"
    seed=1234
    try:
        result=guess_word(guess=guess,seed=seed)
        print("Guess Result: ",result)
    except requests.exceptions.RequestException as e:
        print("An error occured: ", e)

if __name__=="main":
    main()