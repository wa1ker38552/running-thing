from flask import render_template
from flask import redirect
from flask import request
from flask import Flask

from runner import generate_single_runner
from runner import generate_runner_data
from linkedlist import LinkedList
from meet import Meet
import random
import time


# hash table
# initialize database
runner_db = {}
data = generate_runner_data(40)
current_node = data.head
while (current_node.next):
    runner_db[current_node.data.id] = current_node.data
    current_node = current_node.next

schools = ['los altos high school', 'los gatos high school', 'mountain view high school']
def generate_meets_data(amount, runners=50):
    data = LinkedList() # linked list
    for i in range(amount):
        t = (time.time()-random.randint(0, 86400*30))*1000
        name = f'Meet #'+str(random.randint(1, 100))
        participants = []
        # logic to add generated runner to runner db on the go
        for i in range(runners):
            r = generate_single_runner()
            runner_db[r.id] = r
            participants.append(r)

        s = [random.choice(schools)]
        r = random.choice(schools)
        while r in s:
            r = random.choice(schools)
        s.append(r)
        data.append(Meet(name, participants, s, t))

    return data

meet_db = {}
data = generate_meets_data(100)
current_node = data.head
while (current_node.next):
    meet_db[current_node.data.id] = current_node.data
    current_node = current_node.next

app = Flask(__name__)

@app.route('/')
def app_main():
    return render_template('index.html')

@app.route('/runner')
def app_runner():
    rid = request.args.get('id')
    return render_template('runner.html', runner_id=rid)

@app.route('/meet')
def app_meet():
    mid = request.args.get('id')
    return render_template('meet.html', meet_id=mid)

@app.route('/search/runner')
def app_search_runner():
    q = request.args.get('q')
    return render_template('search_runner.html', query=q)

@app.route('/search/meet')
def app_search_meet():
    q = request.args.get('q')
    return render_template('search_meet.html', query=q)

@app.route('/api/search/runner')
def api_search_runner():
    q = request.args.get('q').lower()
    results = []
    for runner in runner_db:
        if q in runner_db[runner].name.lower():
            results.append(runner_db[runner].to_hash_map())
    return results

@app.route('/api/search/meet')
def api_search_meet():
    q = request.args.get('q').lower()
    results = []
    for meet in meet_db:
        if q in meet_db[meet].name.lower():
            m = meet_db[meet].to_hash_map()
            del m['participants']
            results.append(m)
    results = sorted(results, key=lambda x: x['time'])[::-1]
    return results

@app.route('/api/runner')
def api_runner():
    rid = request.args.get('id')
    if rid in runner_db:
        runner = runner_db[rid]
        if runner.time_distributions: # use cache
            return runner.to_hash_map()
        runner.generate_time_distributions(20)
        return runner.to_hash_map()
        
    return {'success': False, 'message': 'Invalid runner ID'}

@app.route('/api/meet')
def api_meet():
    mid = request.args.get('id')
    print(mid)
    if mid in meet_db:
        return meet_db[mid].to_hash_map()
    return {'success': False, 'message': 'Invalid meet ID'}

app.run(host='0.0.0.0', port=8080, debug=True)