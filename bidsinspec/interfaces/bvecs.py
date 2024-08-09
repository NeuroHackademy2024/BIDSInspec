# WIP
# Create a custom Nipype interface that plots the bvec file on a sphere and saves figure
from nipype.interfaces.base import BaseInterfaceInputSpec
from nipype.interfaces.base import File
from nipype.interfaces.base import SimpleInterface
from nipype.interfaces.base import TraitedSpec
from nipype.interfaces.base import traits


class _PlotBvecsInputSpec(BaseInterfaceInputSpec):
    in_file = File(exists=True, mandatory=True, desc="DWI bvec file to be plotted")
    title = traits.Str(desc="a title string for the plot")
    out_file = File("bvec.svg", usedefault=True, desc="output file name")


class _PlotBvecsOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc="written file path")


class PlotBvecs(SimpleInterface):
    """Plot DWI bvecs on a sphere"""

    input_spec = _PlotBvecsInputSpec
    output_spec = _PlotBvecsOutputSpec

    def _run_interface(self, runtime):
        self._results["out_file"] = str(out_file)  # noqa wip

        # need to create a function that plots bvecs on a sphere
        # plot_bvecs()

        return runtime
