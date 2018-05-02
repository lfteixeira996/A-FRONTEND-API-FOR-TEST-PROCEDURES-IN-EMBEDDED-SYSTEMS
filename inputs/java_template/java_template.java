
/*Standard and simops imports*/
import benchConfig.BaseTestSequence;
import project.util.testUtil.PrintUtil;
import simops.base.TestError;
import obswTest.testLib.PrintLib;



public class TEMPLATE_JAVA extends BaseTestSequence {


	/**
     * Sequence
     *
     * @throws TestError in case of error
     */
	public void sequence() throws TestError {

		try {
			mySelf.init();
			// add anything that has to be done before starting the bench here
			mySelf.start();
			initialCondition();

			executeTestcase();
			// add here anything that has to be done before the final checks and before stopping the bench
			mySelf.end();
		}
		catch (Exception e) {
			PrintUtil.printExceptionStackStep(e);
			mySelf.end();
		}
	}


	/**
     * Initial condition
     *
     * @throws TestError in case of error
     */
	public void initialCondition() throws TestError {
		
	}

    /**
     * Execution of all steps in sequence as defined in test specification
     *
     * @throws TestError in case of error
     */
	public void executeTestcase() throws TestError {
		
		
	}

}


