from pathlib import Path

from nipype import IdentityInterface
from nipype.interfaces.io import BIDSDataGrabber
from nipype.pipeline import MapNode
from nipype.pipeline import Node
from nipype.pipeline import Workflow
from nireports.interfaces.fmri import FMRISummary
from nireports.interfaces.mosaic import PlotMosaic


class ReportPipeline:
    def __init__(
        self,
        bids_dir: str | Path,
        output_dir: str | Path,
        name: str = "report_processing",
    ):
        self.name = name
        self.bids_dir = bids_dir
        self.base_dir = output_dir

    def create_workflow(self):
        workflow = Workflow(name=self.name, base_dir=self.base_dir)
        workflow.config["execution"] = {"remove_unnecessary_outputs": False}

        i = 0
        input_node = Node(
            IdentityInterface(
                fields=[
                    "bids_dir",
                ],
            ),
            name="inputnode",
        )

        i += 1
        bids_grab = Node(BIDSDataGrabber(), name=f"{i:02}_BIDSGrabber")

        workflow.connect(input_node, "bids_dir", bids_grab, "base_dir")

        i += 1
        plot_anat = MapNode(
            PlotMosaic(title="Raw T1w"), name=f"{i:02}_PlotAnat", iterfield="in_file"
        )
        workflow.connect(bids_grab, "T1w", plot_anat, "in_file")

        i += 1
        fmri_summary = MapNode(
            FMRISummary(), name=f"{i:02}_FMRISummary", iterfield="in_func"
        )
        workflow.connect(bids_grab, "bold", fmri_summary, "in_func")

        return workflow

    def run(self):
        workflow = self.create_workflow()
        workflow.write_graph("pipeline_flat.dot", graph2use="flat")
        workflow.write_graph("pipeline_hier.dot", graph2use="hierarchical")
        workflow.write_graph("pipeline_col.dot", graph2use="colored")

        in_node = workflow.get_node("inputnode")
        in_node.inputs.bids_dir = self.bids_dir
        workflow.run()
