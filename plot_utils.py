import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


def plot_station_bias(ax,
                      metric_df,
                      vmax,
                      vmin,
                      metric_name,
                      title,
                      dot_sizes,
                      cmap,
                      xlabel=False,
                      ylabel=False):
    lat = metric_df.lat
    lon = metric_df.lon

    m = metric_df[metric_name]
    plt.setp(ax.get_xticklabels(), Fontsize=15)
    plt.setp(ax.get_yticklabels(), Fontsize=15)

    pcm = ax.scatter(lon, lat, c=m,
                     cmap=cmap, s=dot_sizes,
                     vmin=vmin, vmax=vmax)
    ax.set_title(title, fontsize=25)
    if xlabel:
        ax.set_xlabel('lon', fontsize=25)
    if ylabel:
        ax.set_ylabel('lat', fontsize=25)
    return pcm


def Hovmoller_time_test(ax,
                        d_bias_df,
                        ordered_stations,
                        stat_alt_series,
                        vmin,
                        vmax,
                        cmap,
                        idx_method='first',
                        xlabel=True,
                        ylabel=True):
    d_bias_df.index = d_bias_df.time
    date_idx = np.array([str(p)[:10] for i, p in enumerate(d_bias_df.index)])
    d_bias_df = d_bias_df[[c for c in d_bias_df.columns if c != 'time']]
    d_bias_df = d_bias_df[ordered_stations]
    masked_array = np.ma.array(d_bias_df.T, mask=np.isnan(d_bias_df).T).astype(float)

    cmap.set_bad('grey', 1.)
    if vmin > 0:
        img = ax.imshow(masked_array, cmap=cmap, vmin=vmin, vmax=vmax,
                        norm=matplotlib.colors.LogNorm())
    else:
        img = ax.imshow(masked_array, cmap=cmap, vmin=vmin, vmax=vmax)

    i = np.arange(0, len(ordered_stations), int(len(ordered_stations) / 10))

    if idx_method == 'first':
        idx = np.array([int(i) for i, p in enumerate(date_idx) if p[-2:] == '01'])
        date_idx = date_idx[idx]
    else:
        idx = np.arange(0, len(date_idx), 3)
        date_idx = date_idx[idx]
        for d in idx:
            ax.axvline(d - 0.5, c='black')

    _ = ax.set_yticks(i)
    _ = ax.set_yticklabels(stat_alt_series.sort_values(ascending=False).values[i])
    _ = ax.set_xticks(idx)
    _ = ax.set_xticklabels(date_idx, rotation=30)
    if xlabel:
        _ = ax.set_xlabel('time', fontsize=15)
    if ylabel:
        _ = ax.set_ylabel('altitude [m]', fontsize=15)

    return img
