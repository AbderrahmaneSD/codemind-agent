from typing import TypedDict, Annotated, Literal
import operator


class ToolResult(TypedDict):
    tool_name: str
    output: str
    success: bool


class AgentState(TypedDict):
    # --- Input ---
    query: str
    input_type: str
    raw_input: str

    # --- Planning ---
    intent: Literal["review", "debug", "test", "explain", "unknown"]
    plan: list[str]

    # --- Routing + execution ---
    selected_tools: list[str]
    tool_results: Annotated[list[ToolResult], operator.add]

    # --- Critic ---
    critique: str
    score: int
    retry_count: int

    # --- Output ---
    final_answer: str
