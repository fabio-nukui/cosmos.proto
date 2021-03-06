# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/evidence/v1beta1/evidence.proto, cosmos/evidence/v1beta1/genesis.proto, cosmos/evidence/v1beta1/query.proto, cosmos/evidence/v1beta1/tx.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


@dataclass(eq=False, repr=False)
class MsgSubmitEvidence(betterproto.Message):
    """
    MsgSubmitEvidence represents a message that supports submitting arbitrary
    Evidence of misbehavior such as equivocation or counterfactual signing.
    """

    submitter: str = betterproto.string_field(1)
    evidence: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class MsgSubmitEvidenceResponse(betterproto.Message):
    """
    MsgSubmitEvidenceResponse defines the Msg/SubmitEvidence response type.
    """

    # hash defines the hash of the evidence.
    hash: bytes = betterproto.bytes_field(4)


@dataclass(eq=False, repr=False)
class GenesisState(betterproto.Message):
    """GenesisState defines the evidence module's genesis state."""

    # evidence defines all the evidence at genesis.
    evidence: List["betterproto_lib_google_protobuf.Any"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryEvidenceRequest(betterproto.Message):
    """
    QueryEvidenceRequest is the request type for the Query/Evidence RPC method.
    """

    # evidence_hash defines the hash of the requested evidence.
    evidence_hash: bytes = betterproto.bytes_field(1)


@dataclass(eq=False, repr=False)
class QueryEvidenceResponse(betterproto.Message):
    """
    QueryEvidenceResponse is the response type for the Query/Evidence RPC
    method.
    """

    # evidence returns the requested evidence.
    evidence: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryAllEvidenceRequest(betterproto.Message):
    """
    QueryEvidenceRequest is the request type for the Query/AllEvidence RPC
    method.
    """

    # pagination defines an optional pagination for the request.
    pagination: "__base_query_v1_beta1__.PageRequest" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class QueryAllEvidenceResponse(betterproto.Message):
    """
    QueryAllEvidenceResponse is the response type for the Query/AllEvidence RPC
    method.
    """

    # evidence returns all evidences.
    evidence: List["betterproto_lib_google_protobuf.Any"] = betterproto.message_field(1)
    # pagination defines the pagination in the response.
    pagination: "__base_query_v1_beta1__.PageResponse" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class Equivocation(betterproto.Message):
    """
    Equivocation implements the Evidence interface and defines evidence of
    double signing misbehavior.
    """

    height: int = betterproto.int64_field(1)
    time: datetime = betterproto.message_field(2)
    power: int = betterproto.int64_field(3)
    consensus_address: str = betterproto.string_field(4)


class MsgStub(betterproto.ServiceStub):
    async def submit_evidence(
        self,
        *,
        submitter: str = "",
        evidence: "betterproto_lib_google_protobuf.Any" = None,
    ) -> "MsgSubmitEvidenceResponse":

        request = MsgSubmitEvidence()
        request.submitter = submitter
        if evidence is not None:
            request.evidence = evidence

        return await self._unary_unary(
            "/cosmos.evidence.v1beta1.Msg/SubmitEvidence",
            request,
            MsgSubmitEvidenceResponse,
        )


class QueryStub(betterproto.ServiceStub):
    async def evidence(self, *, evidence_hash: bytes = b"") -> "QueryEvidenceResponse":

        request = QueryEvidenceRequest()
        request.evidence_hash = evidence_hash

        return await self._unary_unary(
            "/cosmos.evidence.v1beta1.Query/Evidence", request, QueryEvidenceResponse
        )

    async def all_evidence(
        self, *, pagination: "__base_query_v1_beta1__.PageRequest" = None
    ) -> "QueryAllEvidenceResponse":

        request = QueryAllEvidenceRequest()
        if pagination is not None:
            request.pagination = pagination

        return await self._unary_unary(
            "/cosmos.evidence.v1beta1.Query/AllEvidence",
            request,
            QueryAllEvidenceResponse,
        )


class MsgBase(ServiceBase):
    async def submit_evidence(
        self, submitter: str, evidence: "betterproto_lib_google_protobuf.Any"
    ) -> "MsgSubmitEvidenceResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_submit_evidence(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "submitter": request.submitter,
            "evidence": request.evidence,
        }

        response = await self.submit_evidence(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.evidence.v1beta1.Msg/SubmitEvidence": grpclib.const.Handler(
                self.__rpc_submit_evidence,
                grpclib.const.Cardinality.UNARY_UNARY,
                MsgSubmitEvidence,
                MsgSubmitEvidenceResponse,
            ),
        }


class QueryBase(ServiceBase):
    async def evidence(self, evidence_hash: bytes) -> "QueryEvidenceResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def all_evidence(
        self, pagination: "__base_query_v1_beta1__.PageRequest"
    ) -> "QueryAllEvidenceResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_evidence(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "evidence_hash": request.evidence_hash,
        }

        response = await self.evidence(**request_kwargs)
        await stream.send_message(response)

    async def __rpc_all_evidence(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "pagination": request.pagination,
        }

        response = await self.all_evidence(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/cosmos.evidence.v1beta1.Query/Evidence": grpclib.const.Handler(
                self.__rpc_evidence,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryEvidenceRequest,
                QueryEvidenceResponse,
            ),
            "/cosmos.evidence.v1beta1.Query/AllEvidence": grpclib.const.Handler(
                self.__rpc_all_evidence,
                grpclib.const.Cardinality.UNARY_UNARY,
                QueryAllEvidenceRequest,
                QueryAllEvidenceResponse,
            ),
        }


from ...base.query import v1beta1 as __base_query_v1_beta1__
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
