from fastapi import FastAPI
import random

app = FastAPI()

sessions = {}

@app.get('/api/start_session')
async def start_session():
    session_id = str(random.randint(1000, 10000))
    sessions[session_id] = {'players': {}}
    return {
        'status': 1,
        'message': f'Session with {session_id} has been started.',
        'session_id': session_id
    }

@app.get('/api/join_session')
async def join_session(session_id: str, username: str, choice: str):
    # Checking if session exists.
    if session_id not in sessions:
        return {
            'status': 0,
            'message': f'The session {session_id} does not exist.'
        }
    # Getting sessions players
    session_players = sessions[session_id]['players']
    # Checking if the session has already two players.
    if len(session_players) >= 2:
        return {
            'status': 0,
            'message': 'This session has already two players.'
        }
    # Checking username already exists in the session.
    if username in session_players:
        return {
            'status': 0,
            'message': f'User with username {username} already exist.'
        }
    choices = {'rock', 'paper', 'scissors'}
    if choice.lower() not in choices:
        return {
            'status': 0,
            'message': f"invalid choice. Choose 'rock', 'paper', 'scissors'"
        }
    sessions[session_id]['players'][username] = choice.lower()

    return {
        'status': 1,
        'message': f'{username} has joined session {session_id} with choice {choice.lower()}',
        'players': list(session_players.keys())  # Show current players
    }

@app.get('/api/session_info')
async def session_info(session_id: str):
    # Checking if the sessions exist or not.
    if session_id not in sessions:
        return {
            'status': 0,
            'message': f'Session wih ID {session_id} does not exist.'
        }
    # Getting the session data
    session_players = sessions[session_id]['players']
    if len(session_players) < 2:
        return {
            'status': 1,
            'message': f'Session {session_id} is waiting for more player.',
            'players': list(sessions[session_id]['players'].items())
        }
    # If both player has joined and played the game
    # Here p_1 and p_2 stores the player name and choice in the form of tuple. Eg. (player, choice)
    p_1, p_2 = list(session_players.items())
    # The code below now separates the player and choices.
    p1_name, p1_choice = p_1
    p2_name, p2_choice = p_2
    winner_choices = {('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')}
    
    if p1_choice == p2_choice:
        return {
            'status': 1,
            'message': f'It is draw both players choose {p1_choice}'
        }
    elif (p1_choice, p2_choice) in winner_choices:
        return {
            'status': 1,
            'message': f'{p1_name} is the winnner and he choose {p1_choice} and {p2_name} choose {p2_choice}'
        }
    else:
        return {
            'status': 1,
            'message': f'{p2_name} is the winnner and he choose {p2_choice} and {p1_name} choose {p1_choice}'
        }
