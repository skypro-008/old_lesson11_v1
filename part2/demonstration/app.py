import json

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# ----------
# DEMOS
# ----------

@app.route('/demo2')
def demo2():
    return render_template("episode2/demo.html", name="John", surname="Doe", skill="Python")


@app.route('/demo3')
def demo3():
    return render_template("episode3/demo.html", age=18, img_url="http://via.placeholder.com/150x150")


@app.route('/demo4')
def demo4():
    proxy_servers = {
        "Russia": [
            "252.34.54.158",
            "203.179.83.110",
            "126.203.168.146",
            "217.8.160.216",
            "92.72.191.247",
            "89.153.201.185",
            "236.133.145.210",
            "161.162.118.41",
            "78.246.206.7",
            "252.97.200.38",
            "78.255.251.248",
            "132.84.150.109",
            "199.33.122.27",
            "163.86.83.192",
            "222.151.79.117",
            "173.187.153.160",
            "231.98.233.40",
            "84.195.130.60",
            "8.40.39.119",
            "11.114.130.175",
        ],
        "USA": [
            "253.78.181.252",
            "209.19.222.78",
            "214.129.175.245",
            "4.13.22.7",
            "91.61.169.19",
            "43.111.94.232",
            "148.182.37.201",
            "191.241.254.0",
            "37.124.144.28",
            "23.56.225.27",
            "39.216.160.43",
            "134.42.213.109",
            "233.78.220.145",
            "157.135.13.229",
            "155.108.77.223",
            "237.150.197.214",
            "86.111.216.65",
            "5.9.137.125",
            "83.152.72.1",
            "1.118.18.175",
        ],
        "Brazil": [
            "190.2.79.217",
            "6.72.183.114",
            "172.66.216.40",
            "5.117.181.94",
            "73.245.7.193",
            "124.46.246.97",
            "254.213.189.150",
            "155.60.36.51",
            "77.127.10.81",
            "0.157.191.173",
            "175.48.226.35",
            "94.59.83.230",
            "10.177.199.247",
            "26.83.230.157",
            "106.185.4.244",
            "117.5.142.11",
            "30.33.194.3",
            "182.136.245.187",
            "177.1.134.51",
            "160.192.113.78",
        ]
    }

    return render_template("episode4/demo.html", proxy_servers=proxy_servers)


# ----------
# TASKS
# ----------

@app.route('/task2')
def task2():
    return render_template("episode2/task.html", name="John Doe", speciality="Python Developer", education="BA",
                           jobs=["Google", "Apple", "Microsoft"], img_url="http://via.placeholder.com/150x150")


@app.route('/task3')
def task3():
    dataA = {
        "is_published": True,
        "offers": 10
    }
    dataB = {
        "is_published": False,
    }
    dataC = {
        "is_published": True,
        "offers": 0
    }
    return render_template("episode3/task.html", dataA=dataA, dataB=dataB, dataC=dataC)


@app.route('/task4p1')
def task4_part1():
    data = [
        "Python",
        "Flask",
        "Django",
        "JavaScript",
        "Docker",
        "Kubernetes",
        "nginx"
    ]
    return render_template("episode4/task_part1.html", data=data)


@app.route('/task4p2')
def task4_part2():
    data = {
        "Python": "Middle",
        "Flask": "Advanced",
        "Django": "Senior",
        "JavaScript": "Junior",
        "Docker": "Senior",
        "Kubernetes": "Junior",
        "nginx": "Senior"
    }
    return render_template("episode4/task_part2.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)
