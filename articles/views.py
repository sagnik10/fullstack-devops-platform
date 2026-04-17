from django.shortcuts import render

def article_list(request):
    return render(request,"articles/list.html")


def devops_roadmap(request):
    return render(request,"articles/detail.html",{
        "article_title":"DevOps Roadmap",
        "topics":[
            "Introduction",
            "DevOps Culture",
            "CI/CD",
            "Containers",
            "Infrastructure as Code",
            "Monitoring"
        ]
    })


def docker_guide(request):
    return render(request,"articles/detail.html",{
        "article_title":"Docker Guide",
        "topics":[
            "Introduction",
            "Docker Architecture",
            "Images",
            "Containers",
            "Networking",
            "Docker Compose"
        ]
    })


def kubernetes_basics(request):
    return render(request,"articles/detail.html",{
        "article_title":"Kubernetes Basics",
        "topics":[
            "Introduction",
            "Pods",
            "Deployments",
            "Services",
            "ConfigMaps",
            "Scaling"
        ]
    })


def cicd_pipelines(request):
    return render(request,"articles/detail.html",{
        "article_title":"CI/CD Pipelines",
        "topics":[
            "Introduction",
            "Continuous Integration",
            "Continuous Delivery",
            "Jenkins",
            "GitHub Actions",
            "Deployment Strategies"
        ]
    })