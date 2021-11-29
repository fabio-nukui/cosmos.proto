# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/bank/v1beta1/authz.proto, cosmos/bank/v1beta1/bank.proto, cosmos/bank/v1beta1/genesis.proto, cosmos/bank/v1beta1/query.proto, cosmos/bank/v1beta1/tx.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List, Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


@dataclass(eq=False, repr=False)
class SendAuthorization(betterproto.Message):
    """
    SendAuthorization allows the grantee to spend up to spend_limit coins from
    the granter's account.
    """

    spend_limit: List["__base_v1_beta1__.Coin"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class Params(betterproto.Message):
    """Params defines the parameters for the bank module."""

    send_enabled: List["SendEnabled"] = betterproto.message_field(1)
    default_send_enabled: bool = betterproto.bool_field(2)


@dataclass(eq=False, repr=False)
class SendEnabled(betterproto.Message):
    """
    SendEnabled maps coin denom to a send_enabled status (whether a denom is
    sendable).
    """

    denom: str = betterproto.string_field(1)
    enabled: bool = betterproto.bool_field(2)


@dataclass(eq=False, repr=False)
class Input(betterproto.Message):
    """Input models transaction input."""

    address: str = betterproto.string_field(1)
    coins: List["__base_v1_beta1__.Coin"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class Output(betterproto.Message):
    """Output models transaction outputs."""

    address: str = betterproto.string_field(1)
    coins: List["__base_v1_beta1__.Coin"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class Supply(betterproto.Message):
    """
    Supply represents a struct that passively keeps track of the total supply
    amounts in the network. This message is deprecated now that supply is
    indexed by denom.
    """

    total: List["__base_v1_beta1__.Coin"] = betterproto.message_field(1)

    def __post_init__(self) -> None:
        warnings.warn("Supply is deprecated", DeprecationWarning)
        super().__post_init__()


@dataclass(eq=False, repr=False)
class DenomUnit(betterproto.Message):
    """
    DenomUnit represents a struct that describes a given denomination unit of
    the basic token.
    """

    # denom represents the string name of the given denom unit (e.g uatom).
    denom: str = betterproto.string_field(1)
    # exponent represents power of 10 exponent that one must raise the base_denom
    # to in order to equal the given DenomUnit's denom 1 denom = 1^exponent
    # base_denom (e.g. with a base_denom of uatom, one can create a DenomUnit of
    # 'atom' with exponent = 6, thus: 1 atom = 10^6 uatom).
    exponent: int = betterproto.uint32_field(2)
    # aliases is a list of string aliases for the given denom
    aliases: List[str] = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class Metadata(betterproto.Message):
    """Metadata represents a struct that describes a basic token."""

    description: str = betterproto.string_field(1)
    # denom_units represents the list of DenomUnit's for a given coin
    denom_units: List["DenomUnit"] = betterproto.message_field(2)
    # base represents the base denom (should be the DenomUnit with exponent = 0).
    base: str = betterproto.string_field(3)
    # display indicates the suggested denom that should be displayed in clients.
    display: str = betterproto.string_field(4)
    # name defines the name of the token (eg: Cosmos Atom)
    name: str = betterproto.string_field(5)
    # symbol is the token symbol usually shown on exchanges (eg: ATOM). This can
    # be the same as the display.
    symbol: str = betterproto.string_field(6)


@dataclass(eq=False, repr=False)
class MsgSend(betterproto.Message):
    """
    MsgSend represents a message to send coins from one account to another.
    """

    from_address: str = betterproto.string_field(1)
    to_address: str = betterproto.string_field(2)
    amount: List["__base_v1_beta1__.Coin"] = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class MsgSendResponse(betterproto.Message):
    """MsgSendResponse defines the Msg/Send response type."""

    pass


@dataclass(eq=False, repr=False)
class MsgMultiSend(betterproto.Message):
    """
    MsgMultiSend represents an arbitrary multi-in, multi-out send message.
    """

    inputs: List["Input"] = betterproto.message_field(1)
    outputs: List["Output"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class MsgMultiSendResponse(betterproto.Message):
    """MsgMultiSendResponse defines the Msg/MultiSend response type."""

    pass


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the bank module's genesis state."""

    # params defines all the paramaters of the module.
    params: "Params" = betterproto.message_field(1)
    # balances is an array containing the balances of all the accounts.
    balances: List["Balance"] = betterproto.message_field(2)
    # supply represents the total supply. If it is left empty, then supply will
    # be calculated based on the provided balances. Otherwise, it will be used to
    # validate that the sum of the balances equals this amount.
    supply: List["__base_v1_beta1__.Coin"] = betterproto.message_field(3)
    # denom_metadata defines the metadata of the differents coins.
    denom_metadata: List["Metadata"] = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class Balance(betterproto.Message):
    """
    Balance defines an account address and balance pair used in the bank
    module's genesis state.
    """

    # address is the address of the balance holder.
    address: str = betterproto.string_field(1)
    # coins defines the different coins this balance holds.
    coins: List["__base_v1_beta1__.Coin"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class QueryBalanceRequest(betterproto.Message):
    """
    QueryBalanceRequest is the request type for the Query/Balance RPC method.
    """

    # address is the address to query balances for.
    address: str = betterproto.string_field(1)
    # denom is the coin denom to query balances for.
    denom: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class QueryBalanceResponse(betterproto.Message):
    """
    QueryBalanceResponse is the response type for the Query/Balance RPC method.
    """

    # balance is the balance of the coin.
    balance: "__base_v1_beta1__.Coin" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryAllBalancesRequest(betterproto.Message):
    """
    QueryBalanceRequest is the request type for the Query/AllBalances RPC
    method.
    """

    # address is the address to query balances for.
    address: str = betterproto.string_field(1)
    # pagination defines an optional pagination for the request.
    pagination: "__base_query_v1_beta1__.PageRequest" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class QueryAllBalancesResponse(betterproto.Message):
    """
    QueryAllBalancesResponse is the response type for the Query/AllBalances RPC
    method.
    """

    # balances is the balances of all the coins.
    balances: List["__base_v1_beta1__.Coin"] = betterproto.message_field(1)
    # pagination defines the pagination in the response.
    pagination: "__base_query_v1_beta1__.PageResponse" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class QueryTotalSupplyRequest(betterproto.Message):
    """
    QueryTotalSupplyRequest is the request type for the Query/TotalSupply RPC
    method.
    """

    # pagination defines an optional pagination for the request.
    pagination: "__base_query_v1_beta1__.PageRequest" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryTotalSupplyResponse(betterproto.Message):
    """
    QueryTotalSupplyResponse is the response type for the Query/TotalSupply RPC
    method
    """

    # supply is the supply of the coins
    supply: List["__base_v1_beta1__.Coin"] = betterproto.message_field(1)
    # pagination defines the pagination in the response.
    pagination: "__base_query_v1_beta1__.PageResponse" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class QuerySupplyOfRequest(betterproto.Message):
    """
    QuerySupplyOfRequest is the request type for the Query/SupplyOf RPC method.
    """

    # denom is the coin denom to query balances for.
    denom: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QuerySupplyOfResponse(betterproto.Message):
    """
    QuerySupplyOfResponse is the response type for the Query/SupplyOf RPC
    method.
    """

    # amount is the supply of the coin.
    amount: "__base_v1_beta1__.Coin" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryParamsRequest(betterproto.Message):
    """
    QueryParamsRequest defines the request type for querying x/bank parameters.
    """

    pass


@dataclass(eq=False, repr=False)
class QueryParamsResponse(betterproto.Message):
    """
    QueryParamsResponse defines the response type for querying x/bank
    parameters.
    """

    params: "Params" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryDenomsMetadataRequest(betterproto.Message):
    """
    QueryDenomsMetadataRequest is the request type for the Query/DenomsMetadata
    RPC method.
    """

    # pagination defines an optional pagination for the request.
    pagination: "__base_query_v1_beta1__.PageRequest" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryDenomsMetadataResponse(betterproto.Message):
    """
    QueryDenomsMetadataResponse is the response type for the
    Query/DenomsMetadata RPC method.
    """

    # metadata provides the client information for all the registered tokens.
    metadatas: List["Metadata"] = betterproto.message_field(1)
    # pagination defines the pagination in the response.
    pagination: "__base_query_v1_beta1__.PageResponse" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class QueryDenomMetadataRequest(betterproto.Message):
    """
    QueryDenomMetadataRequest is the request type for the Query/DenomMetadata
    RPC method.
    """

    # denom is the coin denom to query the metadata for.
    denom: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class QueryDenomMetadataResponse(betterproto.Message):
    """
    QueryDenomMetadataResponse is the response type for the Query/DenomMetadata
    RPC method.
    """

    # metadata describes and provides all the client information for the
    # requested token.
    metadata: "Metadata" = betterproto.message_field(1)


class MsgStub(betterproto.ServiceStub):
    async def send(
        self,
        *,
        from_address: str = "",
        to_address: str = "",
        amount: Optional[List["__base_v1_beta1__.Coin"]] = None,
    ) -> "MsgSendResponse":
        amount = amount or []

        request = MsgSend()
        request.from_address = from_address
        request.to_address = to_address
        if amount is not None:
            request.amount = amount

        return await self._unary_unary(
            "/cosmos.bank.v1beta1.Msg/Send", request, MsgSendResponse
        )

    async def multi_send(
        self,
        *,
        inputs: Optional[List["Input"]] = None,
        outputs: Optional[List["Output"]] = None,
    ) -> "MsgMultiSendResponse":
        inputs = inputs or []
        outputs = outputs or []

        request = MsgMultiSend()
        if inputs is not None:
            request.inputs = inputs
        if outputs is not None:
            request.outputs = outputs

        return await self._unary_unary(
            "/cosmos.bank.v1beta1.Msg/MultiSend", request, MsgMultiSendResponse
        )


class QueryStub(betterproto.ServiceStub):
    async def balance(
        self, *, address: str = "", denom: str = ""
    ) -> "QueryBalanceResponse":

        request = QueryBalanceRequest()
        request.address = address
        request.denom = denom

        return await self._unary_unary(
            "/cosmos.bank.v1beta1.Query/Balance", request, QueryBalanceResponse
        )

    async def all_balances(
        self,
        *,
        address: str = "",
        pagination: "__base_query_v1_beta1__.PageRequest" = None,
    ) -> "QueryAllBalancesResponse":

        request = QueryAllBalancesRequest()
        request.address = address
        if pagination is not None:
            request.pagination = pagination

        return await self._unary_unary(
            "/cosmos.bank.v1beta1.Query/AllBalances", request, QueryAllBalancesResponse
        )

    async def total_supply(
        self, *, pagination: "__base_query_v1_beta1__.PageRequest" = None
    ) -> "QueryTotalSupplyResponse":

        request = QueryTotalSupplyRequest()
        if pagination is not None:
            request.pagination = pagination

        return await self._unary_unary(
            "/cosmos.bank.v1beta1.Query/TotalSupply", request, QueryTotalSupplyResponse
        )

    async def supply_of(self, *, denom: str = "") -> "QuerySupplyOfResponse":

        request = QuerySupplyOfRequest()
        request.denom = denom

        return await self._unary_unary(
            "/cosmos.bank.v1beta1.Query/SupplyOf", request, QuerySupplyOfResponse
        )

    async def params(self) -> "QueryParamsResponse":

        request = QueryParamsRequest()

        return await self._unary_unary(
            "/cosmos.bank.v1beta1.Query/Params", request, QueryParamsResponse
        )

    async def denom_metadata(self, *, denom: str = "") -> "QueryDenomMetadataResponse":

        request = QueryDenomMetadataRequest()
        request.denom = denom

        return await self._unary_unary(
            "/cosmos.bank.v1beta1.Query/DenomMetadata",
            request,
            QueryDenomMetadataResponse,
        )

    async def denoms_metadata(
        self, *, pagination: "__base_query_v1_beta1__.PageRequest" = None
    ) -> "QueryDenomsMetadataResponse":

        request = QueryDenomsMetadataRequest()
        if pagination is not None:
            request.pagination = pagination

        return await self._unary_unary(
            "/cosmos.bank.v1beta1.Query/DenomsMetadata",
            request,
            QueryDenomsMetadataResponse,
        )


class MsgBase(ServiceBase):
    async def send(
        self,
        from_address: str,
        to_address: str,
        amount: Optional[List["__base_v1_beta1__.Coin"]],
    ) -> "MsgSendResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def multi_send(
        self, inputs: Optional[List["Input"]], outputs: Optional[List["Output"]]
    ) -> "MsgMultiSendResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_send(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "from_address": request.from_address,
            "to_address": request.to_address,
            "amount": request.amount,
        }

        response = await self.send(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_multi_send(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "inputs": request.inputs,
            "outputs": request.outputs,
        }

        response = await self.multi_send(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.bank.v1beta1.Msg/Send": grpclib.const.Handler(
                self.__rpc_send,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgSend,
                MsgSendResponse,
            ),
            "/cosmos.bank.v1beta1.Msg/MultiSend": grpclib.const.Handler(
                self.__rpc_multi_send,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgMultiSend,
                MsgMultiSendResponse,
            ),
        }


class QueryBase(ServiceBase):
    async def balance(self, address: str, denom: str) -> "QueryBalanceResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def all_balances(
        self, address: str, pagination: "__base_query_v1_beta1__.PageRequest"
    ) -> "QueryAllBalancesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def total_supply(
        self, pagination: "__base_query_v1_beta1__.PageRequest"
    ) -> "QueryTotalSupplyResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def supply_of(self, denom: str) -> "QuerySupplyOfResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def params(self) -> "QueryParamsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def denom_metadata(self, denom: str) -> "QueryDenomMetadataResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def denoms_metadata(
        self, pagination: "__base_query_v1_beta1__.PageRequest"
    ) -> "QueryDenomsMetadataResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_balance(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "address": request.address,
            "denom": request.denom,
        }

        response = await self.balance(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_all_balances(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "address": request.address,
            "pagination": request.pagination,
        }

        response = await self.all_balances(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_total_supply(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "pagination": request.pagination,
        }

        response = await self.total_supply(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_supply_of(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "denom": request.denom,
        }

        response = await self.supply_of(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_params(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {}

        response = await self.params(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_denom_metadata(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "denom": request.denom,
        }

        response = await self.denom_metadata(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_denoms_metadata(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "pagination": request.pagination,
        }

        response = await self.denoms_metadata(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.bank.v1beta1.Query/Balance": grpclib.const.Handler(
                self.__rpc_balance,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryBalanceRequest,
                QueryBalanceResponse,
            ),
            "/cosmos.bank.v1beta1.Query/AllBalances": grpclib.const.Handler(
                self.__rpc_all_balances,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAllBalancesRequest,
                QueryAllBalancesResponse,
            ),
            "/cosmos.bank.v1beta1.Query/TotalSupply": grpclib.const.Handler(
                self.__rpc_total_supply,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryTotalSupplyRequest,
                QueryTotalSupplyResponse,
            ),
            "/cosmos.bank.v1beta1.Query/SupplyOf": grpclib.const.Handler(
                self.__rpc_supply_of,
                grpclib.const.Cardinality.UNARY_UNARY,
                QuerySupplyOfRequest,
                QuerySupplyOfResponse,
            ),
            "/cosmos.bank.v1beta1.Query/Params": grpclib.const.Handler(
                self.__rpc_params,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryParamsRequest,
                QueryParamsResponse,
            ),
            "/cosmos.bank.v1beta1.Query/DenomMetadata": grpclib.const.Handler(
                self.__rpc_denom_metadata,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryDenomMetadataRequest,
                QueryDenomMetadataResponse,
            ),
            "/cosmos.bank.v1beta1.Query/DenomsMetadata": grpclib.const.Handler(
                self.__rpc_denoms_metadata,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryDenomsMetadataRequest,
                QueryDenomsMetadataResponse,
            ),
        }


from ...base import v1beta1 as __base_v1_beta1__
from ...base.query import v1beta1 as __base_query_v1_beta1__
