"""Chart generation in the deal-book theme (navy / grey, RdYlGn heatmaps)."""
from __future__ import annotations
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from . import config
from .dcf import enterprise_value
from .sensitivity import per_share_grid
from .comps import trading_comps, precedent_transactions

P = config.PALETTE
plt.rcParams.update({"font.family": "Liberation Sans", "font.size": 10.5,
                     "axes.axisbelow": True, "figure.dpi": 150})


def _clean(ax):
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color("#999999")
    ax.spines["bottom"].set_color("#333333")
    ax.tick_params(colors=P["ink"], labelsize=9.5)


def football_field(a, outdir):
    ev = enterprise_value(a)
    tc = trading_comps(a); pc = precedent_transactions(a)
    grid = per_share_grid(a)
    dcf_lo = grid.loc["5.5x", "9.5%"]; dcf_hi = grid.loc["6.5x", "8.5%"]
    rows = [("DCF (WACC 8.5-9.5%, exit 5.5-6.5x)", dcf_lo, dcf_hi),
            ("Trading comps (6.0-7.5x)", tc["ps_low"], tc["ps_high"]),
            ("Precedent txns (7.0-9.0x)", pc["ps_low"], pc["ps_high"]),
            ("52-week trading range", 9.0, 22.0)]
    fig, ax = plt.subplots(figsize=(7.2, 3.9))
    cols = [P["navy"], P["blue"], P["steel"], P["lgrey"]]
    for i, (lbl, lo, hi) in enumerate(rows):
        ax.barh(i, hi - lo, left=lo, height=0.5, color=cols[i])
        ax.text(lo - 0.3, i, f"${lo:.0f}", va="center", ha="right", fontsize=8.5, color=P["ink"])
        ax.text(hi + 0.3, i, f"${hi:.0f}", va="center", ha="left", fontsize=8.5, color=P["ink"])
    ax.axvline(a.offer_price, color=P["red"], lw=1.8, ls="--")
    ax.text(a.offer_price, len(rows) - 0.35, f"  Offer ${a.offer_price:.2f}", color=P["red"],
            fontweight="bold", fontsize=9.5)
    ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows], fontsize=9)
    ax.set_xlabel("Equity value per share ($)", fontsize=9.5); ax.set_xlim(0, 40)
    ax.set_title("Organon — Valuation Football Field ($/share)", color="#000000",
                 fontsize=12.5, fontweight="bold", pad=10, loc="left")
    ax.invert_yaxis(); _clean(ax); ax.grid(axis="x", color="#E6E6E6"); ax.grid(axis="y", visible=False)
    path = os.path.join(outdir, "py_football_field.png")
    fig.tight_layout(); fig.savefig(path, bbox_inches="tight"); plt.close()
    return path


def sensitivity_heatmap(a, outdir):
    grid = per_share_grid(a)
    M = grid.values
    fig, ax = plt.subplots(figsize=(7.1, 4.0))
    im = ax.imshow(M, cmap="RdYlGn", aspect="auto")
    ax.set_xticks(range(grid.shape[1])); ax.set_xticklabels(grid.columns)
    ax.set_yticks(range(grid.shape[0])); ax.set_yticklabels(grid.index)
    ax.set_xlabel("WACC", fontsize=9.5); ax.set_ylabel("Terminal EV/EBITDA exit", fontsize=9.5)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            ax.text(j, i, f"${M[i, j]:.0f}", ha="center", va="center",
                    color="#111111", fontsize=9.5, fontweight="bold")
    ax.set_title("DCF Sensitivity — Equity Value / Share ($)", color="#000000",
                 fontsize=12, fontweight="bold", pad=10, loc="left")
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.03).set_label("$/share", fontsize=8.5)
    path = os.path.join(outdir, "py_sensitivity.png")
    fig.tight_layout(); fig.savefig(path, bbox_inches="tight"); plt.close()
    return path


def dcf_summary_bar(a, outdir):
    ev = enterprise_value(a)
    fig, ax = plt.subplots(figsize=(7.0, 3.7))
    labels = ["PV of FCF", "PV of TV", "Enterprise\nvalue", "(-) Net debt", "Equity\nvalue"]
    vals = [ev["pv_fcf"], ev["pv_tv"], ev["ev"], -a.net_debt, ev["equity"]]
    cols = [P["steel"], P["blue"], P["navy"], P["grey"], P["navy"]]
    bars = ax.bar(labels, vals, color=cols, width=0.6)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + (200 if v >= 0 else -400),
                f"${v:,.0f}", ha="center", fontsize=9, color=P["ink"], fontweight="bold")
    ax.set_ylabel("US$ mm", fontsize=9.5)
    ax.set_title(f"DCF Build — EV \\${ev['ev']:,.0f}m   |   \\${ev['per_share']:.1f}/share",
                 color="#000000", fontsize=12, fontweight="bold", pad=10, loc="left")
    _clean(ax); ax.axhline(0, color="#333333", lw=0.8)
    path = os.path.join(outdir, "py_dcf_build.png")
    fig.tight_layout(); fig.savefig(path, bbox_inches="tight"); plt.close()
    return path


def generate_all(a, outdir):
    os.makedirs(outdir, exist_ok=True)
    return [football_field(a, outdir), sensitivity_heatmap(a, outdir), dcf_summary_bar(a, outdir)]
