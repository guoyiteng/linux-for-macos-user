store.set_global_value('hotkey', '<meta>+c')

if re.match('.*(Hyper)', window.get_active_class()):
    logging.debug('terminal')
    engine.set_return_value('<ctrl>+<shift>+c')
else:
    logging.debug('normal')
    engine.set_return_value('<ctrl>+c')
    
engine.run_script('combo')