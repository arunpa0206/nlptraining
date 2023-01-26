!pip install transformers

from transformers import pipeline
from transformers.pipelines.pt_utils import KeyDataset
from tqdm.auto import tqdm

text = """As what geographers have estimated, about twenty percent of the earth’s surface is occupied by deserts. A majority of us view deserts as one unique kind of landscape — areas with little or no rainfalls.
In actual fact, there are differences between the deserts, though in varying degrees. While it is common for laymen like us to see deserts as rocky or covered with gravel or pebbles, there are some where large sand dunes inhabit. Despite the fact that rainfall is minimal, temperatures do change in deserts, ranging from seasonal ones to daily changes where extreme hotness and coldness are experienced in the day and night. Unfavorable conditions in the deserts, especially the lack of water, have discouraged many living things from inhabiting these landscapes. Nevertheless, there are exceptionally surviving ones which through their superb tactics, have managed to live through and are still going strong. One such kind is the specialist annual plants which overcome seasonal temperature changes with their extremely short, active life cycles.
In events of sudden rain, the plant seeds pullulate and grow very quickly to make full use of the rain water. Their flowers bloom and set seeds that ripen quickly in the hot sun too. Once the water runs dry, the mother plant dies, leaving behind the drought-resistant seeds, waiting patiently for the next rainy season to arrive. The Cacti, a native in American deserts, adapts to the dry surroundings by having unique body structures. The plant has swollen stems to help store water that carries it through months. By having sharp pines instead of leaves, water loss through respiration is minimized. Besides, these pointed pines also help the plant ward off grazing animals, thus enhancing its survival period. Besides plants, there are also animals with distinct surviving tactics in deserts too."""

summarizer = pipeline("summarization")
summarized = summarizer(text, min_length=75, max_length=300)

summary =' '.join([str(i) for i in summarized])

print(summary)
