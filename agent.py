# agent.py

import http.client
import json
from together import Together

def ticket_booking_agent(source, destination, mode):
    try:
        conn = http.client.HTTPSConnection("google.serper.dev")
        payload = json.dumps({
            "q": f"Trip from {source} to {destination} via {mode}. Provide options, price, timing, etc."
        })
        headers = {
            'X-API-KEY': "64880c44ef37384040dc253c954ed2f190c0e4702c3e80745e5eb78221f47376"',
            'Content-Type': 'application/json'
        }
        conn.request("POST", "/search", payload, headers)
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")
    except Exception as e:
        return f"Error in ticket_booking_agent: {e}"

def ticket_booking_agent_1(destination, source, mode):
    try:
        conn = http.client.HTTPSConnection("google.serper.dev")
        payload = json.dumps({
            "q": f"Trip from {destination} to {source} via {mode}. Provide options, price, timing, etc."
        })
        headers = {
            'X-API-KEY': '92f001a3eb91d20af265a2c7a4bba43e1f2bd200',
            'Content-Type': 'application/json'
        }
        conn.request("POST", "/search", payload, headers)
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")
    except Exception as e:
        return f"Error in ticket_booking_agent_1: {e}"

def outing_planner_agent(destination, days, ih):
    try:
        conn = http.client.HTTPSConnection("google.serper.dev")
        payload = json.dumps({
            "q": f"Plan for {days} days at {destination}, focusing on interests: {ih}. Include important places, hotels with prices, restaurants, transport, etc."
        })
        headers = {
            'X-API-KEY': '92f001a3eb91d20af265a2c7a4bba43e1f2bd200',
            'Content-Type': 'application/json'
        }
        conn.request("POST", "/search", payload, headers)
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")
    except Exception as e:
        return f"Error in outing_planner_agent: {e}"

def generate_response(prompt, model, api_key, max_tokens, temperature):
    try:
        together_client = Together(api_key=api_key)
        response = together_client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a trip guide assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=1,
            top_k=50,
            repetition_penalty=1,
            stop=[""]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error with Together API: {e}"
