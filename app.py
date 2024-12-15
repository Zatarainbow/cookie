from flask import Flask, request, jsonify

app = Flask(__name__)

# Đường dẫn gốc, nơi nhận dữ liệu POST
@app.route('/api/post_data', methods=['POST'])
def post_data():
    try:
        # Lấy dữ liệu từ POST request
        data = request.json
        # Ghi dữ liệu vào file (hoặc cơ sở dữ liệu)
        with open('data_log.txt', 'a') as file:
            file.write(str(data) + '\n')
        return jsonify({"status": "success", "message": "Data received and saved!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
