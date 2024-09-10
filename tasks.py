# tasks.py

from agent import ticket_booking_agent, ticket_booking_agent_1, outing_planner_agent, generate_response
from tools import save_text_as_docx
import streamlit as st

def generate_trip_plan(source, destination, mode, days, ih):
    # Fetch data
    agent_1_data = ticket_booking_agent(source, destination, mode)
    agent_1_1_data = ticket_booking_agent_1(destination, source, mode)
    agent_2_data = outing_planner_agent(destination, days, ih)

    # Generate responses
    api_key = "64880c44ef37384040dc253c954ed2f190c0e4702c3e80745e5eb78221f47376"
    model = "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo"
    
    agent_1_output = generate_response(f"Explain this: {agent_1_data}", model, api_key, 500, 0.11)
    agent_1_1_output = generate_response(f"Explain this: {agent_1_1_data}", model, api_key, 500, 0.11)
    agent_2_output = generate_response(f"Plan this: {agent_2_data}", model, api_key, 1000, 0.21)
    
    # Save and return document
    final = f'{agent_1_output}\n\n{agent_1_1_output}\n\n{agent_2_output}'
    filename = 'Trip_details.docx'
    save_text_as_docx(final, filename)
    return filename
