from django.shortcuts import render
from jchart import Chart
from jchart.config import Axes, DataSet, rgba


class PieChart(Chart):
    chart_type = 'pie'

    def get_labels(self, **kwargs):
        return ["Red", "Blue", "Yellow"]

    def get_datasets(self, **kwargs):
        data = [300, 50, 100]
        colors = [
            "#FF6384",
            "#36A2EB",
            "#FFCE56"
        ]
        return [DataSet(data=data,
                        label="My Pie Data",
                        backgroundColor=colors,
                        hoverBackgroundColor=colors)]


def index(request):
    return render(request, 'base.html')


def some_view(request):
    return render(request, 'first_chart.html', {
        'line_chart': PieChart(),
    })

