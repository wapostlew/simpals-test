import strawberry

from . import queries, mutations, subscriptions

schema = strawberry.Schema(
    query=queries.Query,
    mutation=mutations.Mutation,
    subscription=subscriptions.Subscription,
)
