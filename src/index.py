from types import ModuleType
from typing import Any, Callable
from app import app
from dash import html, dcc, Output, Input
import dash_bootstrap_components as dbc
import os
import importlib
from dataclasses import dataclass


@dataclass(frozen=True)
class Report:
    id: str
    name: str
    layout: Any


reports: dict[str, Report] = dict()
for report_filename in os.listdir("reports"):
    if "__" in report_filename:
        continue
    report_id = report_filename[:-3]
    reports[report_id] = Report(
        id=report_id,
        name=report_id.replace("_", " "),
        layout=importlib.import_module(f"reports.{report_id}").layout,
    )


app.layout = html.Div(
    children=[
        url := dcc.Location(id="url", refresh=False),
        dbc.NavbarSimple(
            links_left=True,
            brand="Home",
            brand_href="/",
            children=[
                dbc.NavItem(dbc.NavLink(report.name, href=f"/{report_id}"))
                for report in reports.values()
            ],
        ),
        dbc.Container(
            children=[
                title := html.H4(""),
                body := html.Div(),
            ]
        ),
    ],
)


@app.callback(
    Output(title, "children"),
    Output(body, "children"),
    Input(url, "pathname"),
)
def load_content(url: str):
    try:
        # parse the report id
        try:
            (_,report_id) = url.split("/")
        except Exception as e:
            raise Exception(f"Invalid url: {url}")

        # if base url
        if not report_id:
            return "Home", None

        # if in a report
        if report_id not in reports:
            raise Exception(f"Report {report_id} not found")
        report = reports[report_id]
        return report.name, report.layout

        # if none of the conditions are met
        raise Exception(f"Invalid url: {url}")
    except Exception as e:
        return f"Error: {e.__class__.__name__}", dbc.Label(repr(e))


if __name__ == "__main__":
    app.run()
