def sharks_seen_evolution_heatmap(df_ultimos_anyos):

    import seaborn as sns
    import matplotlib.pyplot as plt
    import plotly.express as px
    sns.set_theme()

    cmap = sns.color_palette("coolwarm", as_cmap=True)

    shark_seen_evolution = df_ultimos_anyos.pivot_table(index="month", columns="year", values=["name"], aggfunc = "count")
    f, ax = plt.subplots(figsize=(9, 6))
    sns.heatmap(shark_seen_evolution, annot=True,cmap=cmap , linewidths=.5, ax=ax)


def top_week_day_graph(df_ultimos_anyos):

    import seaborn as sns
    import matplotlib.pyplot as plt
    import plotly.express as px
    sns.set_theme()
    
    sharks_per_day_country = df_ultimos_anyos.groupby(["country", "week_day"])["name"].count().reset_index()

    top_countries = list(sharks_per_day_country.groupby("country")["name"].sum().reset_index().sort_values(by="name", ascending=False).head(10)["country"])

    sharks_per_day_country.sort_values(by="name", ascending=False)

    data_frame_for_graph = sharks_per_day_country[sharks_per_day_country['country'].isin(top_countries)]

    fig = px.bar(data_frame_for_graph, x='week_day', y="name", color='country',
             hover_data=['country'],
             title='Días de la semana donde más tiburones se ven')
    fig.show()


def number_of_sharks_per_country_graph(df_ultimos_anyos):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import plotly.express as px
    sns.set_theme()

    sharks_per_month_country = df_ultimos_anyos.groupby(["country", "month"])["name"].count().reset_index()

    countries_top_sharks = list(sharks_per_month_country.groupby("country")["name"].sum().reset_index().sort_values(by="name", ascending=False).head(10)["country"])

    sharks_per_month_country.sort_values(by="name", ascending=False)

    data_frame_for_graph_3 = sharks_per_month_country[sharks_per_month_country['country'].isin(countries_top_sharks)]

    fig = px.line(data_frame_for_graph_3, x="month", y="name",
              color="country",
              hover_data={"name": "|%B %d, %Y", "country": True},
              title='Países y meses donde se ven más tiburones')

    fig.update_yaxes(showticklabels=True, ticktext=countries_top_sharks)

    fig.update_layout(
        legend=dict(
            orientation="v",
            xanchor="right",
            y=1
        )
    )
    fig.show()


def number_of_sharks_per_state_graph(df_ultimos_anyos):
    import seaborn as sns
    import matplotlib.pyplot as plt
    import plotly.express as px
    sns.set_theme()

    sharks_per_state = df_ultimos_anyos.groupby(["state", "country"])["date"].agg("count").reset_index().rename(columns={"date":"shark"})

    sharks_per_state = sharks_per_state.sort_values(by = 'shark', ascending=False)

    sharks_per_state = sharks_per_state.head(int(len(sharks_per_state) * 0.1))

    state_top_attacks = list(sharks_per_state["state"])

    fig = px.pie(sharks_per_state, values='shark', names='state', title='Top ciudades donde ver tiburones')
    fig.show()


def number_of_sharks_per_location_graph(df_ultimos_anyos):

    import seaborn as sns
    import matplotlib.pyplot as plt
    import plotly.express as px
    sns.set_theme()

    attacks_per_location = df_ultimos_anyos.groupby(["location", "country"])["date"].agg("count").reset_index().rename(columns={"date":"attack"})
    attacks_per_location = attacks_per_location.sort_values(by = 'attack', ascending=False)
    location_top_attacks = attacks_per_location.head(10)  # Seleccionamos solo las 10 primeras entradas
    attacks_per_location = attacks_per_location [location_top_attacks.isin(location_top_attacks)]
    fig = px.pie(attacks_per_location, values='attack', names='location', title='Top localizaciones donde ver tiburones')
    fig.show()


def top_species_graph(df_ultimos_anyos):

    import seaborn as sns
    import matplotlib.pyplot as plt
    import plotly.express as px
    sns.set_theme()

    species_seen = df_ultimos_anyos.groupby(["species"])["date"].agg("count").reset_index().rename(columns={"date":"shark"})

    species_seen = species_seen.sort_values(by = 'shark', ascending=False)

    species_seen = species_seen.head(int(len(species_seen) * 0.1))

    state_top_species = list(species_seen["species"])

    fig = px.pie(species_seen, values='shark', names='species', title='Especies de tiburones más vistas')
    fig.show()

