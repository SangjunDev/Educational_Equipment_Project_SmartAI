from SmartAI import socketio, app

if __name__ == '__main__':

    socketio.run(app,port=8080, debug=True)