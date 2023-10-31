# Copyright 2020 by B. Knueven, D. Mildebrath, C. Muir, J-P Watson, and D.L. Woodruff
# This software is distributed under the 3-clause BSD License.
# This is an extension to be used for testing.
# Not all extension points are guaranteed to be here (see the parent class)


import mpisppy.utils.sputils as sputils
import mpisppy.extensions.xhatbase
import mpisppy.phbase as phbase

class TestExtension(mpisppy.extensions.extension.Extension):
    """
    Args:
        spo (SPOpt object): the calling object
    """
    def __init__(self, spo):
        super().__init__(spo)
        self.who_is_called = list()

        
    def pre_solve(self, subproblem):
        self.who_is_called.append("pre_solve")

        
    def post_solve_loop(self):
        self.who_is_called.append("post_solve_loop")

        
    def post_solve(self, subproblem, results):
        self.who_is_called.append("post_solve")
        return results

        
    def pre_iter0(self):
        self.who_is_called.append("pre_iter0")

        
    def post_iter0(self):
        self.who_is_called.append("post_iter0")


    def post_iter0_after_sync(self):
        self.who_is_called.append("post_iter0_after_sync")
        
        
    def miditer(self):
        self.who_is_called.append("miditer")

    
    def enditer(self):
        self.who_is_called.append("enditer")

        
    def enditer_after_sync(self):        
        self.who_is_called.append("enditer_after_sync")

        
    def post_everything(self):
        self.who_is_called.append("post_everything")
        # make it easy to find out who has been called
        self.opt._TestExtension_who_is_called = self.who_is_called

