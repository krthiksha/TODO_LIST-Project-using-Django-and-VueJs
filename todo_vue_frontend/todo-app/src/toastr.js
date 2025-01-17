
import toastr from 'toastr';   //toaster is already available after installing adminLTE (check in nodeModules)
import 'toastr/build/toastr.min.css';

export function useToastr() {

    toastr.options.positionClass = 'toast-bottom-right';
    toastr.options.closeButton = true;
    toastr.options.progressBar = true;
    toastr.options.timeOut = 2500;

    return toastr;
}