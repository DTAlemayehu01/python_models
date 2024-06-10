import numpy as np
import plotly.graph_objects as go
import scipy.constants

P = np.linspace(-20,20,200)
V = np.linspace(-20,20,200)
P,V = np.meshgrid(P,V)

k = scipy.constants.k
#T = -0.01
#avogadro's No.
AgN = scipy.constants.N_A

#Using Lowercase t to dentoe temperature
C = lambda p,v,t : (p*v)/(k*t*AgN)

fig = go.Figure()

# Add traces, one for each slider step
for T in np.arange(20, 200, 0.8):
    fig.add_trace(
        go.Surface(
            visible=False,
            name="Temperature = " + str(T),
            x=P, y=V, z=C(P,V,T)))

# Make 10th trace visible
fig.data[10].visible = True

# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": "Slider switched to step: " + str(i)}],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Frequency: "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    scene = dict(
        xaxis = dict(nticks=4, range=[-20,20],),
        yaxis = dict(nticks=4, range=[-20,20],),
        zaxis = dict(nticks=4, range=[-2.5,2.5],),
        xaxis_title="Pressure (Pa)",
        yaxis_title="Volume (m^3)",
        zaxis_title="Mols",),
    title="Mols of an ideal gas as a function of Pressure and Volume",
    sliders=sliders
)

#fig.show()
fig.write_html("Concentration.html")
