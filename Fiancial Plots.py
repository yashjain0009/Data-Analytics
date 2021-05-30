import mpl_finance as mpf
import matplotlib.pyplot as plt
start = (2014, 5, 1)
end = (2014, 6, 30)
quotes = mpf.quotes_historical_yahoo('^GDAXI', start, end)
fig, ax = plt.subplots(figsize=(8, 5))
fig.subplots_adjust(bottom=0.2)
mpf.candlestick(ax, quotes, width=0.6, colorup='b', colordown='r')
plt.grid(True)
ax.xaxis_date()
# dates on the x-axis
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=30)