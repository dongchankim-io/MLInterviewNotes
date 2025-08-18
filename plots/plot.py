import numpy as np
import matplotlib.pyplot as plt

# ---------- activation functions ----------
def sigmoid(z): return 1/(1+np.exp(-z))
def tanh_fn(z): return np.tanh(z)
def relu(z): return np.maximum(0.0, z)
def leaky_relu(z, a=0.1): return np.where(z >= 0, z, a*z)
def elu(z, alpha=1.0): return np.where(z >= 0, z, alpha*(np.exp(z)-1))
def gelu_approx(z):  # Hendrycks & Gimpel tanh approximation
    return 0.5*z*(1 + np.tanh(np.sqrt(2/np.pi)*(z + 0.044715*z**3)))
def swish(z): return z * sigmoid(z)

# GLU/SwiGLU (1D slices just to visualize gating trend)
def glu_slice(z):    return z * sigmoid(z)
def swiglu_slice(z): return z * swish(z)

# ---------- THEMING ----------
FIG_BG   = "#0b1020"   # dark figure background
AX_BG    = "#141e2f"   # slightly brighter axes background
FG       = "#e6f7ff"   # bright foreground (text/ticks)
AXIS_CLR = "#ffffff"   # axis lines at 0
LINE_CLR = "#00e5ff"   # plot curve

LINE_KW = dict(color=LINE_CLR, linewidth=3.2, solid_capstyle="round")

# ---------- minimal axes helper ----------
def minimal_axes(ax, xlim, ylim, title):
    # background colors
    ax.set_facecolor(AX_BG)
    # hide spines; draw only axis lines at 0
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.axhline(0, linewidth=1.2, color=AXIS_CLR)
    ax.axvline(0, linewidth=1.2, color=AXIS_CLR)
    # ticks only at 0 and 1 (bright)
    #ax.set_xticks([0, 1]); ax.set_yticks([0, 1])
    ax.set_xticks([0]); ax.set_yticks([0])
    ax.tick_params(length=3, labelsize=9, colors=FG)
    # ranges + title
    ax.set_xlim(*xlim); #ax.set_ylim(*ylim)
    ax.set_title(title, fontsize=12, pad=6, color=FG)
    # square panel
    try: ax.set_box_aspect(1)
    except AttributeError: ax.set_aspect('equal', adjustable='box')

# ---------- domains & shared ranges ----------
X_RANGE = (-2, 2)
x = np.linspace(*X_RANGE, 2000)

# Softmax: vary one logit t; plot P(class1) as others fixed to 0
t = x.copy()
logits = np.vstack([t, np.zeros_like(t), np.zeros_like(t)])
exp_logits = np.exp(logits - logits.max(axis=0, keepdims=True))
softmax = exp_logits / exp_logits.sum(axis=0, keepdims=True)
p_class1 = softmax[0]

# Shared Y range across all charts
curves = [
    relu(x), leaky_relu(x, 0.1), tanh_fn(x), sigmoid(x), elu(x, 1.0),
    gelu_approx(x), swish(x), glu_slice(x), swiglu_slice(x), p_class1
]
y_min = float(min(np.min(c) for c in curves))
y_max = float(max(np.max(c) for c in curves))
pad_lo, pad_hi = 0.05*(abs(y_min)+1), 0.05*(abs(y_max)+1)
Y_RANGE = (y_min - pad_lo, y_max + pad_hi)

# ---------- plotting  ----------
fig, axes = plt.subplots(3, 4, figsize=(17, 12))
fig.patch.set_facecolor(FIG_BG)                 # dark figure background
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
plt.subplots_adjust(wspace=0, hspace=0.5)     # widen chart gaps

plots = [
    ("ReLU",                    x, relu(x)),
    ("Leaky ReLU (a=0.1)",     x, leaky_relu(x, a=0.1)),
    ("tanh",                    x, tanh_fn(x)),
    ("Sigmoid",                 x, sigmoid(x)),
    ("ELU (α=1)",               x, elu(x, alpha=1.0)),
    ("GELU (tanh approx)",      x, gelu_approx(x)),
    ("Swish / SiLU",            x, swish(x)),
    ("GLU (1D slice)",          x, glu_slice(x)),
    ("SwiGLU (1D slice)",       x, swiglu_slice(x)),
    ("Softmax: P(class 1) vs t",t, p_class1),
]

for ax, (title, xv, yv) in zip(axes.ravel(), plots):
    ax.plot(xv, yv, **LINE_KW)
    minimal_axes(ax, X_RANGE, Y_RANGE, title)

# Paint the remaining (unused) subplots with AX_BG and hide everything
for ax in axes.ravel()[len(plots):]:
    ax.set_facecolor(FIG_BG)          # same card color as other subplots
    ax.set_title("")                 # no title
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():    # no borders
        sp.set_visible(False)
    # don't draw 0-axes lines

# Save with figure background preserved
plt.savefig("activations_5x2_dark_theme.png", dpi=600, facecolor=FIG_BG, edgecolor=FIG_BG, bbox_inches="tight")
plt.show()
print("Saved to activations_5x2_dark_theme.png")
