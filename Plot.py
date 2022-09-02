import pandas as pd
from plot_utils import plot_station_bias, Hovmoller_time_test
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


sat = 'HelioMont'
HM_dt_df = pd.read_excel('SatBiasMetrics/{}daytime_stat_metrics.xlsx'.format(sat))
HM_df = pd.read_excel('SatBiasMetrics/{}daynighttime_stat_metrics.xlsx'.format(sat))
HM_sac_df = pd.read_excel('SatBiasMetrics/SACRAM_{}daynighttime_stat_metrics.xlsx'.format(sat))
HM_sac_dt_df = pd.read_excel('SatBiasMetrics/SACRAM_{}daytime_stat_metrics.xlsx'.format(sat))
HM_seasonal_dt_df = pd.read_excel('SatBiasMetrics/{}_seasonal_daytime_stat_metrics.xlsx'.format(sat))


sat = 'HelioSat'
HS_dt_df = pd.read_excel('SatBiasMetrics/{}daytime_stat_metrics.xlsx'.format(sat))
HS_df = pd.read_excel('SatBiasMetrics/{}daynighttime_stat_metrics.xlsx'.format(sat))
HS_sac_df = pd.read_excel('SatBiasMetrics/SACRAM_{}daynighttime_stat_metrics.xlsx'.format(sat))
HS_sac_dt_df = pd.read_excel('SatBiasMetrics/SACRAM_{}daytime_stat_metrics.xlsx'.format(sat))
HS_seasonal_dt_df = pd.read_excel('SatBiasMetrics/{}_seasonal_daytime_stat_metrics.xlsx'.format(sat))


cols = HM_df.columns.tolist()
cols[0] = 'station'
HM_df.columns = cols

dt_cols = HM_dt_df.columns.tolist()
dt_cols[0] = 'station'
HM_dt_df.columns = dt_cols

cols = HS_df.columns.tolist()
cols[0] = 'station'
HS_df.columns = cols

dt_cols = HS_dt_df.columns.tolist()
dt_cols[0] = 'station'
HS_dt_df.columns = dt_cols

cols = HS_sac_df.columns.tolist()
cols[0] = 'station'
HS_sac_df.columns = cols

cols = HM_sac_df.columns.tolist()
cols[0] = 'station'
HM_sac_df.columns = cols

cols = HS_sac_dt_df.columns.tolist()
cols[0] = 'station'
HS_sac_dt_df.columns = cols

cols = HM_sac_dt_df.columns.tolist()
cols[0] = 'station'
HM_sac_dt_df.columns = cols

HM_seasonal_dt_df['station'] = HM_seasonal_dt_df.index
HS_seasonal_dt_df['station'] = HS_seasonal_dt_df.index

dot_sizes = (HM_dt_df.alt.values/HM_dt_df.alt.max())*200

fig, axes = plt.subplots(2, 2,
                         figsize=(12, 6),
                         sharex=True,
                         sharey=True,
                         constrained_layout=True)

pcm = plot_station_bias(axes[0,0],
                        metric_df=HM_dt_df,
                        vmax=120,
                        vmin=-120,
                        metric_name='bias',
                        title='MBD',
                        dot_sizes=dot_sizes,
                        cmap='seismic',
                        xlabel=False,
                        ylabel=True)

pcm = plot_station_bias(axes[0,1],
                        metric_df=HS_dt_df,
                        vmax=120,
                        vmin=-120,
                        metric_name='bias',
                        title='MBD',
                        dot_sizes=dot_sizes,
                        cmap='seismic',
                        xlabel=False,
                        ylabel=False)

ticks = np.arange(-120,140,40)
cbar = fig.colorbar(pcm, ax=axes[0], location='right',
                    fraction=0.1, ticks=ticks)
cbar.ax.set_ylabel('W/m2', fontsize=15)
tick_labels = [str(s) for s in ticks]
tick_labels[0] = '<'+tick_labels[0]
tick_labels[-1] = '>'+tick_labels[-1]
_ = cbar.ax.set_yticklabels(tick_labels, fontsize=15)

pcm = plot_station_bias(axes[1,0],
                        metric_df=HM_dt_df,
                        vmax=180,
                        vmin=0,
                        metric_name='rmse',
                        title='RMSD',
                        dot_sizes=dot_sizes,
                        cmap='jet',
                        xlabel=True,
                        ylabel=True)

pcm = plot_station_bias(axes[1,1],
                        metric_df=HS_dt_df,
                        vmax=180,
                        vmin=0,
                        metric_name='rmse',
                        title='RMSD',
                        dot_sizes=dot_sizes,
                        cmap='jet',
                        xlabel=True,
                        ylabel=False)

ticks = list(np.arange(0,200,40))
ticks.append(180)
cbar = fig.colorbar(pcm, ax=axes[-1], location='right',
                    fraction=0.1, ticks=ticks)
cbar.ax.set_ylabel('W/m2', fontsize=15)

tick_labels = [str(s) for s in ticks]
tick_labels[-1] = '>'+tick_labels[-1]
_ = cbar.ax.set_yticklabels(tick_labels, fontsize=15)
fig.savefig('Initial_scatter_plot.png')

dot_sizes = (HM_dt_df.alt.values/HM_dt_df.alt.max())*200

fig, axes = plt.subplots(4, 2,
                         figsize=(12, 12),
                         sharex=True,
                         sharey=True,
                         constrained_layout=True)

pcm = plot_station_bias(axes[0,0],
                        metric_df=HM_dt_df,
                        vmax=120,
                        vmin=0,
                        metric_name='rmse',
                        title='Inst. RMSD',
                        dot_sizes=dot_sizes,
                        cmap='jet',
                        xlabel=False,
                        ylabel=True)

pcm = plot_station_bias(axes[0,1],
                        metric_df=HS_dt_df,
                        vmax=120,
                        vmin=0,
                        metric_name='rmse',
                        title='Inst. RMSD',
                        dot_sizes=dot_sizes,
                        cmap='jet',
                        xlabel=False,
                        ylabel=False)

pcm = plot_station_bias(axes[1,0],
                        metric_df=HM_dt_df,
                        vmax=120,
                        vmin=0,
                        metric_name='h_rmse',
                        title='Hourly RMSD',
                        dot_sizes=dot_sizes,
                        cmap='jet',
                        xlabel=False,
                        ylabel=True)

pcm = plot_station_bias(axes[1,1],
                        metric_df=HS_dt_df,
                        vmax=120,
                        vmin=0,
                        metric_name='h_rmse',
                        title='Hourly RMSD',
                        dot_sizes=dot_sizes,
                        cmap='jet',
                        xlabel=False,
                        ylabel=False)

pcm = plot_station_bias(axes[2,0],
                        metric_df=HM_dt_df,
                        vmax=120,
                        vmin=0,
                        metric_name='d_rmse',
                        title='Daily RMSD',
                        dot_sizes=dot_sizes,
                        cmap='jet',
                        xlabel=False,
                        ylabel=True)

pcm = plot_station_bias(axes[2,1],
                        metric_df=HS_dt_df,
                        vmax=120,
                        vmin=0,
                        metric_name='d_rmse',
                        title='Daily RMSD',
                        dot_sizes=dot_sizes,
                        cmap='jet',
                        xlabel=False,
                        ylabel=False)

pcm = plot_station_bias(axes[3,0],
                        metric_df=HM_dt_df,
                        vmax=120,
                        vmin=0,
                        metric_name='m_rmse',
                        title='Monthly RMSD',
                        dot_sizes=dot_sizes,
                        cmap='jet',
                        xlabel=True,
                        ylabel=True)

pcm = plot_station_bias(axes[3,1],
                        metric_df=HS_dt_df,
                        vmax=120,
                        vmin=0,
                        metric_name='m_rmse',
                        title='Monthly RMSD',
                        dot_sizes=dot_sizes,
                        cmap='jet',
                        xlabel=True,
                        ylabel=False)

ticks = np.arange(0,140,20)
cbar = fig.colorbar(pcm, ax=axes[-1], location='bottom',
                    fraction=0.1, ticks=ticks)
cbar.ax.set_xlabel('W/m2', fontsize=15)

tick_labels = [str(s) for s in ticks]
tick_labels[-1] = '>'+tick_labels[-1]
cbar.ax.set_xticklabels(tick_labels, fontsize=15)
fig.savefig('Different_aggregations_rmse_plot.png')


dot_sizes = (HM_dt_df.alt.values/HM_dt_df.alt.max())*200

fig, axes = plt.subplots(4, 2,
                         figsize=(12, 12),
                         sharex=True,
                         sharey=True,
                         constrained_layout=True)

pcm = plot_station_bias(axes[0,0],
                        metric_df=HM_seasonal_dt_df,
                        vmax=120,
                        vmin=-120,
                        metric_name='s_bias',
                        title='Spring MBD',
                        dot_sizes=dot_sizes,
                        cmap='seismic',
                        xlabel=False,
                        ylabel=True)

pcm = plot_station_bias(axes[0,1],
                        metric_df=HS_seasonal_dt_df,
                        vmax=120,
                        vmin=-120,
                        metric_name='s_bias',
                        title='Spring MBD',
                        dot_sizes=dot_sizes,
                        cmap='seismic',
                        xlabel=False,
                        ylabel=False)

pcm = plot_station_bias(axes[1,0],
                        metric_df=HM_seasonal_dt_df,
                        vmax=120,
                        vmin=-120,
                        metric_name='sm_bias',
                        title='Summer MBD',
                        dot_sizes=dot_sizes,
                        cmap='seismic',
                        xlabel=False,
                        ylabel=True)

pcm = plot_station_bias(axes[1,1],
                        metric_df=HS_seasonal_dt_df,
                        vmax=120,
                        vmin=-120,
                        metric_name='sm_bias',
                        title='Summer MBD',
                        dot_sizes=dot_sizes,
                        cmap='seismic',
                        xlabel=False,
                        ylabel=False)

pcm = plot_station_bias(axes[2,0],
                        metric_df=HM_seasonal_dt_df,
                        vmax=120,
                        vmin=-120,
                        metric_name='a_bias',
                        title='Autumn MBD',
                        dot_sizes=dot_sizes,
                        cmap='seismic',
                        xlabel=False,
                        ylabel=True)

pcm = plot_station_bias(axes[2,1],
                        metric_df=HS_seasonal_dt_df,
                        vmax=120,
                        vmin=-120,
                        metric_name='a_bias',
                        title='Autumn MBD',
                        dot_sizes=dot_sizes,
                        cmap='seismic',
                        xlabel=False,
                        ylabel=False)

pcm = plot_station_bias(axes[3,0],
                        metric_df=HM_seasonal_dt_df,
                        vmax=120,
                        vmin=-120,
                        metric_name='w_bias',
                        title='Winter MBD',
                        dot_sizes=dot_sizes,
                        cmap='seismic',
                        xlabel=True,
                        ylabel=True)

pcm = plot_station_bias(axes[3,1],
                        metric_df=HS_seasonal_dt_df,
                        vmax=120,
                        vmin=-120,
                        metric_name='w_bias',
                        title='Winter MBD',
                        dot_sizes=dot_sizes,
                        cmap='seismic',
                        xlabel=True,
                        ylabel=False)

ticks = np.arange(-120,140,40)
cbar = fig.colorbar(pcm, ax=axes[-1], location='bottom',
                    fraction=0.1, ticks=ticks)
cbar.ax.set_xlabel('W/m2', fontsize=15)

tick_labels = [str(s) for s in ticks]
tick_labels[0] = '<'+tick_labels[0]
tick_labels[-1] = '>'+tick_labels[-1]
_ = cbar.ax.set_xticklabels(tick_labels, fontsize=15)
fig.savefig('Seasonal_bias_plot.png')


sat = 'HelioMont'
hm_bias_df = pd.read_excel('SatBiasMetrics/{}_d_bias_df.xlsx'.format(sat))
hm_rmse_df = pd.read_excel('SatBiasMetrics/{}_d_rmse_df.xlsx'.format(sat))

sat = 'HelioSat'
hs_bias_df = pd.read_excel('SatBiasMetrics/{}_d_bias_df.xlsx'.format(sat))
hs_rmse_df = pd.read_excel('SatBiasMetrics/{}_d_rmse_df.xlsx'.format(sat))

stat_alt_series = HM_df.sort_values('alt').alt
stations = HM_df.sort_values('alt', ascending=False).station.tolist()

fig,ax = plt.subplots(2,2,sharex=True,
                       sharey=True,
                       figsize=(15,6))
ax[0,0].set_title('MBD', fontsize=20)
img = Hovmoller_time_test(ax[0,0],
                    hm_bias_df,
                    stations,
                    stat_alt_series,
                    -275,
                    275,
                    cmap=matplotlib.cm.seismic,
                    xlabel=False,
                    ylabel=False)

ax[0,1].set_title('MBD', fontsize=20)
img = Hovmoller_time_test(ax[0,1],
                    hs_bias_df,
                    stations,
                    stat_alt_series,
                    -275,
                    275,
                    cmap=matplotlib.cm.seismic,
                    xlabel=False,
                    ylabel=False)

cbar = fig.colorbar(img, orientation='vertical', ax=ax[0], ticks=[-275,-200,-100,0,100, 200, 275])
cbar.ax.set_yticklabels(labels=['<-275','-200','-100','0','100', '200', '>275'])
cbar.ax.set_ylabel('W/m2', rotation=90)

ax[1,0].set_title('RMSD', fontsize=20)
img = Hovmoller_time_test(ax[1,0],
                    hm_rmse_df,
                    stations,
                    stat_alt_series,
                    0,
                    250,
                    cmap=matplotlib.cm.viridis,
                    xlabel=False,
                    ylabel=False)

ax[1,1].set_title('RMSD', fontsize=20)
img = Hovmoller_time_test(ax[1,1],
                    hs_rmse_df,
                    stations,
                    stat_alt_series,
                    0,
                    250,
                    cmap=matplotlib.cm.viridis,
                    xlabel=False,
                    ylabel=False)

cbar = fig.colorbar(img, orientation='vertical', ax=ax[1], ticks=[0,50,150,250])
cbar.ax.set_yticklabels(labels=['0', '50', '150', '>250'])
_ = cbar.ax.set_ylabel('W/m2', rotation=90)

fig.savefig('Hovmoller_plot.png')